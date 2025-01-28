import streamlit as st
import PyPDF2
import openai
import os
from langchain.document_loaders import PyPDFLoader, TextLoader
from langchain.chains import RetrievalQA
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import FAISS

def load_pdf(file):
    """Loads a PDF file and extracts text from it.

    Args:
        file: A PDF file object.

    Returns:
        str: Extracted text from the PDF.
    """
    pdf_reader = PyPDF2.PdfReader(file)
    text = ""
    for page in pdf_reader.pages:
        text += page.extract_text()
    return text

def load_text(file):
    """Loads a text file and reads its content.

    Args:
        file: A text file object.

    Returns:
        str: Content of the text file.
    """
    text = file.read().decode("utf-8")
    return text

def query_openai(prompt):
    """Queries the OpenAI API with a given prompt.

    Args:
        prompt: A string containing the prompt to send to OpenAI.

    Returns:
        str: The response content from OpenAI.
    """
    openai.api_key = os.getenv("OPENAI_API_KEY")
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message['content']

def langchain_qa(file_content):
    """Performs question answering using Langchain.

    Args:
        file_content: The content of the file to perform QA on.

    Returns:
        str: The answer to the question.
    """
    embeddings = OpenAIEmbeddings()
    vector_store = FAISS.from_texts([file_content], embeddings)
    qa_chain = RetrievalQA.from_chain_type(llm=openai.ChatCompletion, chain_type="stuff", retriever=vector_store.as_retriever())
    return qa_chain.run(question)

st.title("PDF and Text File Question Answering with OpenAI")

uploaded_file = st.sidebar.file_uploader("Choose a PDF or text file", type=["pdf", "txt"])

if uploaded_file is not None:
    if uploaded_file.type == "application/pdf":
        pdf_text = load_pdf(uploaded_file)
        st.write("Document Content:", pdf_text)
    elif uploaded_file.type == "text/plain":
        text_content = load_text(uploaded_file)
        st.write("Document Content:", text_content)

    question = st.text_input("Ask a question about the document content:")
    
    if st.button("Get Answer"):
        if question:
            if uploaded_file.type == "application/pdf":
                answer = langchain_qa(pdf_text)
            elif uploaded_file.type == "text/plain":
                answer = langchain_qa(text_content)
            st.write("Answer:", answer)
        else:
            st.warning("Please enter a question.")