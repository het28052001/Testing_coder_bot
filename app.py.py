from fastapi import FastAPI, HTTPException, Form
from pydantic import BaseModel, HttpUrl
import httpx

app = FastAPI()

class GitHubCredentials(BaseModel):
    github_url: HttpUrl
    username: str
    access_token: str

@app.post("/validate-github/")
async def validate_github(credentials: GitHubCredentials):
    async with httpx.AsyncClient() as client:
        response = await client.get(
            f"{credentials.github_url}/user",
            auth=(credentials.username, credentials.access_token)
        )
        if response.status_code == 200:
            return {"message": "Validation successful"}
        else:
            raise HTTPException(status_code=response.status_code, detail="Validation failed")