import streamlit as st
import PyPDF2
import openai
import os

# Set OpenAI API key
openai.api_key = os.getenv("OPENAI_API_KEY")

def read_pdf(file):
    pdf_reader = PyPDF2.PdfReader(file)
    text = ""
    for page in pdf_reader.pages:
        text += page.extract_text()
    return text

def ask_openai(question, context):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": f"Context: {context}\nQuestion: {question}"}
        ]
    )
    answer = response['choices'][0]['message']['content']
    return answer

st.title("PDF Question Answering App")

uploaded_file = st.file_uploader("Upload a PDF file", type="pdf")

if uploaded_file is not None:
    context = read_pdf(uploaded_file)
    st.write("PDF content loaded successfully.")

    question = st.text_input("Ask a question about the PDF:")
    
    if st.button("Get Answer"):
        if question:
            answer = ask_openai(question, context)
            st.write("Answer:", answer)
        else:
            st.write("Please enter a question.")