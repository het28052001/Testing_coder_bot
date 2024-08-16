from fastapi import FastAPI, File, UploadFile
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.post("/uploadfile/")
async def upload_file(file: UploadFile = File(...)):
    contents = await file.read()
    return {"filename": file.filename, "content_type": file.content_type, "size": len(contents)}

@app.get("/", response_class=HTMLResponse)
async def main():
    content = """
    <form action="/uploadfile/" enctype="multipart/form-data" method="post">
        <input name="file" type="file">
        <input type="submit">
    </form>
    """
    return content