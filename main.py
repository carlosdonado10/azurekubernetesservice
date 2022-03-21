from fastapi import FastAPI
from fastapi.exceptions import HTTPException
from azure.identity import DefaultAzureCredential
from datetime import datetime

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}


@app.get('/today')
async def get_today():
    return datetime.now()


@app.get('/credential')
async def get_today():
    credential = DefaultAzureCredential()
    return 'success'
