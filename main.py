from fastapi import FastAPI

app = FastAPI(title = 'API da Raira')

@app.get("/")
def hello():
    return("message:" "Hello, world!")