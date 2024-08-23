import streamlit as st
import PyPDF2
import openai
import os
from bs4 import BeautifulSoup

def load_pdf(file):
    pdf_reader = PyPDF2.PdfReader(file)
    text = ""
    for page in pdf_reader.pages:
        text += page.extract_text()
    return text

def load_text(file):
    text = file.read().decode("utf-8")
    return text

def load_html(file):
    soup = BeautifulSoup(file.read(), 'html.parser')
    return soup.get_text()

def query_openai(prompt):
    openai.api_key = os.getenv("OPENAI_API_KEY")
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message['content']

st.title("PDF, Text, and HTML File Question Answering with OpenAI")

uploaded_file = st.sidebar.file_uploader("Choose a PDF, text, or HTML file", type=["pdf", "txt", "html"])

if uploaded_file is not None:
    if uploaded_file.type == "application/pdf":
        pdf_text = load_pdf(uploaded_file)
        st.write("Document Content:", pdf_text)
    elif uploaded_file.type == "text/plain":
        text_content = load_text(uploaded_file)
        st.write("Document Content:", text_content)
    elif uploaded_file.type == "text/html":
        html_content = load_html(uploaded_file)
        st.write("Document Content:", html_content)

    question = st.text_input("Ask a question about the document content:")
    
    if st.button("Get Answer"):
        if question:
            if uploaded_file.type == "application/pdf":
                answer = query_openai(f"{pdf_text}\n\nQuestion: {question}")
            elif uploaded_file.type == "text/plain":
                answer = query_openai(f"{text_content}\n\nQuestion: {question}")
            elif uploaded_file.type == "text/html":
                answer = query_openai(f"{html_content}\n\nQuestion: {question}")
            st.write("Answer:", answer)
        else:
            st.warning("Please enter a question.")