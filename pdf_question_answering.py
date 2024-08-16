import streamlit as st
import PyPDF2
import openai
import os
from fastapi import FastAPI, UploadFile, File
from fastapi.responses import JSONResponse
import uvicorn

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

@app.post("/uploadfile/")
async def create_upload_file(file: UploadFile = File(...), question: str = None):
    if file.content_type == "application/pdf":
        pdf_text = load_pdf(await file.read())
        answer = query_openai(f"{pdf_text}\n\nQuestion: {question}") if question else "No question provided."
    elif file.content_type == "text/plain":
        text_content = load_text(await file.read())
        answer = query_openai(f"{text_content}\n\nQuestion: {question}") if question else "No question provided."
    else:
        return JSONResponse(content={"error": "Invalid file type"}, status_code=400)
    
    return JSONResponse(content={"answer": answer})

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

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)