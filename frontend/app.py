from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.middleware.cors import CORSMiddleware
from fastapi.templating import Jinja2Templates
import uvicorn  
import requests
import logging
from var2 import backend_ip

backend_url = f"http://{backend_ip}:9567"
app = FastAPI()
templates = Jinja2Templates(directory="templates")


app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://34.47.230.139:9567"],
    allow_credentials=True,
    allow_methods=["GET", "POST"],
    allow_headers=["*"],
)

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# root endpoint
@app.get("/", response_class = HTMLResponse)
async def root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "backend_url": backend_url})

# insert endpoint
@app.post("/insert")
async def insert_doc(request: Request):
    data = await request.json()
    responses = requests.post(backend_url + "/insert", json = data).json()
    logger.info("Inserting to db...")
    return responses

# search endpoint
@app.get("/search")
async def search_(query):
    return requests.get(backend_url + "/search", params = {"query": query}).json()

if __name__ == "__main__":
    uvicorn.run(app, host = "0.0.0.0", port = 9567)