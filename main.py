from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get("/")
def read_root():
    return HTMLResponse("<h1>Welcome to CrossBridge</h1>")
