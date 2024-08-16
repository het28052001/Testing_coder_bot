import streamlit as st
import PyPDF2
import openai
import os

def load_pdf(file):
    pdf_reader = PyPDF2.PdfReader(file)
    text = ""
    for page in pdf_reader.pages:
        text += page.extract_text()
    return text

def load_text(file):
    text = file.read().decode("utf-8")
    return text

def query_openai(prompt):
    openai.api_key = os.getenv("OPENAI_API_KEY")
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message['content']

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
                answer = query_openai(f"{pdf_text}\n\nQuestion: {question}")
            elif uploaded_file.type == "text/plain":
                answer = query_openai(f"{text_content}\n\nQuestion: {question}")
            st.write("Answer:", answer)
        else:
            st.warning("Please enter a question.")

# README.md

# Project Title

## Description

This project is designed to demonstrate how to set up a Python virtual environment and run a Streamlit application.

## Setup Instructions

1. **Create a Virtual Environment**
   This command creates a new virtual environment named `venv`. A virtual environment is a self-contained directory that contains a Python installation for a particular version of Python, plus several additional packages.
   ```bash
   python3 -m venv venv
   ```

2. **Activate the Virtual Environment**
   This command activates the virtual environment. Once activated, any Python or pip commands will use the versions in the virtual environment instead of the global Python installation.
   ```bash
   source venv/bin/activate
   ```

3. **Install Required Packages**
   This command installs all the necessary packages listed in the `requirements.txt` file. These packages are essential for the application to run properly.
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Streamlit Application**
   This command starts the Streamlit application by running the `main.py` file. Streamlit will open a new tab in your web browser to display the application interface.
   ```bash
   streamlit run main.py
   ```