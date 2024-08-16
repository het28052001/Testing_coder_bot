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

def github_api(access_token, username, github_url):
    headers = {
        'Authorization': f'token {access_token}',
        'Accept': 'application/vnd.github.v3+json'
    }
    response = requests.get(github_url, headers=headers)
    if response.status_code == 200:
        return response.json(), 200
    else:
        return {'error': response.json()}, response.status_code

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

access_token = st.text_input("GitHub Access Token:")
username = st.text_input("GitHub Username:")
github_url = st.text_input("GitHub URL:")

if st.button("Get GitHub Data"):
    if access_token and username and github_url:
        data, status_code = github_api(access_token, username, github_url)
        if status_code == 200:
            st.write("GitHub Data:", data)
        else:
            st.error(data['error'])
    else:
        st.warning("Please enter all GitHub details.")