from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.middleware.cors import CORSMiddleware
from elasticsearch import Elasticsearch
import uvicorn  
import requests
import logging
from var2 import backend_ip

backend_url = f"http://{backend_ip}:9567"
app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://35.200.255.237:9567"],
    allow_credentials=True,
    allow_methods=["GET", "POST"],
    allow_headers=["*"],
)

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

es_host = "elasticsearch"
es_port = 9200
index_name = "myindex"
log_file = "logs.json"

def get_es_connection():
    try:
        es = Elasticsearch(
            [f"http://{es_host}:{es_port}"],
            request_timeout=30,
            max_retries=3,
            retry_on_timeout=True,
            sniff_on_start=False,
            sniff_on_node_failure=False
        )
        
        if not es.ping():
            raise ConnectionError("Error")
            
        logger.info("Successfully connected Elasticsearch")
        return es
    
    except ConnectionError as e:
        logger.error(f"Elasticsearch connection failed: {str(e)}")
        raise HTTPException(status_code = 500, detail = "Service Unavailable - connection failed")

es = get_es_connection()

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