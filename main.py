
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"status": "GOALMASTER LITE is alive!"}
