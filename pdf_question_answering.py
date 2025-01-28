import streamlit as st
import PyPDF2
import openai
import os

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