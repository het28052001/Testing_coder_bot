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
    response = requests.get(f"https://api.github.com/repos/{credentials.username}/{credentials.repo_url.split('/')[-1]}", headers=headers)

    if response.status_code == 200:
        return {"status": "valid"}
    else:
        raise HTTPException(status_code=401, detail="Invalid credentials")