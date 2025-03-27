from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
import uvicorn  
import requests
import logger
from var2 import backend_ip

backend_url = f"http://{backend_ip}:9567"
app = FastAPI()

# root endpoint
@app.get("/", response_class = HTMLResponse)
async def root():
    with open("index.html", "r") as f:
        html_content = f.read()
    return HTMLResponse(content = html_content)

# insert endpoint
@app.post("/insert")
async def insert_doc(request):
    data = await request.json()
    responses = requests.post(backend_url + "/insert", json = data).json
    logger.info("Inserting to db...")
    return 

# search endpoint
@app.get("/search")
async def search_(query):
    return requests.get(backend_url + "/search", params = {"query": query}).json

if __name__ == "__main__":
    uvicorn.run(app, host = "0.0.0.0", port = 9567)