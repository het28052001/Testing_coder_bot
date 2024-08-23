import streamlit as st
import os

def load_html(file):
    with open(file, 'r', encoding='utf-8') as f:
        return f.read()

def display_html(file):
    html_content = load_html(file)
    st.components.v1.html(html_content, height=600)

def upload_html_file():
    uploaded_file = st.file_uploader("Upload an HTML file", type=["html"])
    if uploaded_file is not None:
        with open(os.path.join("tempDir", uploaded_file.name), "wb") as f:
            f.write(uploaded_file.getbuffer())
        display_html(os.path.join("tempDir", uploaded_file.name))