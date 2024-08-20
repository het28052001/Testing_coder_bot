from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import requests

app = FastAPI()

class Credentials(BaseModel):
    repo_url: str
    access_token: str
    username: str

@app.post("/validate_credentials/")
async def validate_credentials(credentials: Credentials):
    headers = {
        "Authorization": f"token {credentials.access_token}"
    }
    response = requests.get(f"https://api.github.com/repos/{credentials.username}/{credentials.repo_url}", headers=headers)
    
    if response.status_code == 200:
        return {"status": "valid"}
    else:
        raise HTTPException(status_code=400, detail="Invalid credentials")

import streamlit as st
import requests

st.title("GitHub Credentials Validator")

repo_url = st.text_input("GitHub Repo URL")
access_token = st.text_input("GitHub Access Token", type="password")
username = st.text_input("GitHub Username")

if st.button("Validate"):
    response = requests.post("http://localhost:8000/validate_credentials/", json={
        "repo_url": repo_url,
        "access_token": access_token,
        "username": username
    })
    
    if response.status_code == 200:
        st.success("Credentials are valid!")
    else:
        st.error("Invalid credentials!")