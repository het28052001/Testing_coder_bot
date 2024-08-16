from fastapi import FastAPI, File, UploadFile
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.post("/uploadfile/")
async def upload_file(file: UploadFile = File(...)):
    with open(file.filename, "wb") as f:
        content = await file.read()
        f.write(content)
    return {"filename": file.filename}

@app.get("/", response_class=HTMLResponse)
async def main():
    content = """
    <form action="/uploadfile/" enctype="multipart/form-data" method="post">
    <input name="file" type="file">
    <input type="submit">
    </form>
    """
    return HTMLResponse(content=content)