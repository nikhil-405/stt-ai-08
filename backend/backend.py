from fastapi import FastAPI, Query
from elasticsearch import Elasticsearch
import uvicorn
from var import elastic_search_ip

es = Elasticsearch([f"http://{elastic_search_ip}:5500"])
app = FastAPI()

# backend function to handle searching among the available documents
@app.get("/search")
def search(query):
    response = es.search(index = "db", body = {"query": {"match": {"text": query}}})
    if response["hits"]["hits"]:
        return response["hits"]["hits"]
    return "Match not found in available documents!!"

# backend function to insert a large document to the ElasticSearch index
@app.post("/insert")
def insert(text):
    doc = {"text": text}
    es.index(index = "db", body = doc)
    return {"message": "Inserted successfully!"}

if __name__ == "__main__":
    uvicorn.run(app, host = "0.0.0.0", port = 9567)