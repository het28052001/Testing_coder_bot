import streamlit as st
import PyPDF2
import openai
import os
import requests

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

def validate_credentials(repo_url, access_token, username):
    headers = {
        "Authorization": f"token {access_token}"
    }
    response = requests.get(f"https://api.github.com/repos/{username}/{repo_url.split('/')[-1]}", headers=headers)

    if response.status_code == 200:
        return {"status": "valid"}
    else:
        return {"status": "invalid"}

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

repo_url = st.text_input("Enter GitHub Repo URL:")
access_token = st.text_input("Enter GitHub Access Token:", type="password")
username = st.text_input("Enter GitHub Username:")

if st.button("Validate Credentials"):
    if repo_url and access_token and username:
        validation_result = validate_credentials(repo_url, access_token, username)
        st.write("Validation Result:", validation_result)
    else:
        st.warning("Please fill in all fields.")