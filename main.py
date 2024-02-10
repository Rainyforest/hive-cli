from typing import Union
from db import get_all_words
import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "http://localhost:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def health():
    return {"status": "200 OK"}

@app.get("/words")
def read_item():
    return {"words": get_all_words()[:100]}


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", log_level="info")