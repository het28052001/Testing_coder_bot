import streamlit as st  
import PyPDF2  
import openai  
import os  

def load_pdf(file):  
    """  
    Loads a PDF file and extracts text from it.  
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

def query_openai(prompt):  
    """  
    Queries the OpenAI API with a given prompt.  
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

st.title("Pdf chatbot")  
st.write("Upload a PDF document and ask questions about its content.")  

uploaded_file = st.file_uploader("Choose a PDF file", type="pdf")  

if uploaded_file is not None:  
    pdf_text = load_pdf(uploaded_file)  
    st.text_area("PDF Content", pdf_text, height=300)  

    question = st.text_input("Ask a question about the PDF content:")  
    
    if st.button("Get Answer"):  
        if question:  
            answer = query_openai(f"{pdf_text}\n\nQuestion: {question}")  
            st.write("Answer:", answer)  
        else:  
            st.warning("Please enter a question.")  