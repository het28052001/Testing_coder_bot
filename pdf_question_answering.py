import streamlit as st
import PyPDF2
import openai
import os
import httpx

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

async def validate_github(credentials):
    async with httpx.AsyncClient() as client:
        response = await client.get(
            f"{credentials['github_url']}/user",
            auth=(credentials['username'], credentials['access_token'])
        )
        if response.status_code == 200:
            return {"message": "Validation successful"}
        else:
            raise Exception("Validation failed")

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

    github_url = st.text_input("GitHub URL:")
    username = st.text_input("Username:")
    access_token = st.text_input("Access Token:", type="password")

    if st.button("Validate GitHub"):
        if github_url and username and access_token:
            credentials = {
                "github_url": github_url,
                "username": username,
                "access_token": access_token
            }
            try:
                validation_response = validate_github(credentials)
                st.write(validation_response)
            except Exception as e:
                st.error(str(e))
        else:
            st.warning("Please fill in all fields.")