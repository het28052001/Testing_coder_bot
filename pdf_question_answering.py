import streamlit as st
import PyPDF2
import openai
import os
from sentence_transformers import SentenceTransformer
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

def load_pdf(file):
    pdf_reader = PyPDF2.PdfReader(file)
    text = ""
    for page in pdf_reader.pages:
        text += page.extract_text()
    return text

def load_text(file):
    text = file.read().decode("utf-8")
    return text

def chunk_text(text, chunk_size=500):
    return [text[i:i + chunk_size] for i in range(0, len(text), chunk_size)]

def generate_embeddings(text_chunks):
    model = SentenceTransformer('all-MiniLM-L6-v2')
    return model.encode(text_chunks)

def query_openai(prompt):
    openai.api_key = os.getenv("OPENAI_API_KEY")
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message['content']

def retrieve_similar_chunk(question, text_chunks, embeddings):
    model = SentenceTransformer('all-MiniLM-L6-v2')
    question_embedding = model.encode([question])
    similarities = cosine_similarity(question_embedding, embeddings)
    most_similar_index = np.argmax(similarities)
    return text_chunks[most_similar_index]

st.title("PDF and Text File Question Answering with OpenAI")

uploaded_file = st.sidebar.file_uploader("Choose a PDF or text file", type=["pdf", "txt"])

if uploaded_file is not None:
    if uploaded_file.type == "application/pdf":
        pdf_text = load_pdf(uploaded_file)
        st.write("Document Content:", pdf_text)
        text_chunks = chunk_text(pdf_text)
        embeddings = generate_embeddings(text_chunks)
    elif uploaded_file.type == "text/plain":
        text_content = load_text(uploaded_file)
        st.write("Document Content:", text_content)
        text_chunks = chunk_text(text_content)
        embeddings = generate_embeddings(text_chunks)

    question = st.text_input("Ask a question about the document content:")
    
    if st.button("Get Answer"):
        if question:
            similar_chunk = retrieve_similar_chunk(question, text_chunks, embeddings)
            answer = query_openai(f"{similar_chunk}\n\nQuestion: {question}")
            st.write("Answer:", answer)
        else:
            st.warning("Please enter a question.")