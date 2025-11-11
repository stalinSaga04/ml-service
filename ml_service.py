from fastapi import FastAPI, UploadFile, File
from fastapi.responses import JSONResponse
import tempfile, os, json

app = FastAPI()

@app.get("/")
def root():
    return {"message": "ML service is running successfully 🚀"}

@app.post("/analyze")
async def analyze_video(file: UploadFile = File(...)):
    with tempfile.NamedTemporaryFile(delete=False, suffix=".mp4") as tmp:
        contents = await file.read()
        tmp.write(contents)
        path = tmp.name

    # Just return mock data for now
    result = [
        {"id": 1, "start": "00:00:00", "end": "00:00:05", "emotion": "happy", "shotType": "wide", "keep": True},
        {"id": 2, "start": "00:00:05", "end": "00:00:10", "emotion": "sad", "shotType": "close", "keep": True}
    ]

    os.remove(path)
    return JSONResponse(content=result)
