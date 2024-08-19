import streamlit as st
import PyPDF2
import openai
import os
from fastapi import FastAPI
import uvicorn
import requests

app = FastAPI()

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

@app.post("/get_answer/")
async def get_answer(prompt: str):
    return {"answer": query_openai(prompt)}

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
                prompt = f"{pdf_text}\n\nQuestion: {question}"
            elif uploaded_file.type == "text/plain":
                prompt = f"{text_content}\n\nQuestion: {question}"
            response = requests.post("http://127.0.0.1:8000/get_answer/", json={"prompt": prompt})
            answer = response.json().get("answer")
            st.write("Answer:", answer)
        else:
            st.warning("Please enter a question.")

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)