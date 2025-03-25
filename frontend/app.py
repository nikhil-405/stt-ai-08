from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import uvicorn

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
async def root():
    with open("index.html", "r") as f:
        html_content = f.read()
    return HTMLResponse(content = html_content, status_code = 200)

if __name__ == "__main__":
    uvicorn.run(app, host = "0.0.0.0", port = 9567)