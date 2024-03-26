
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
import os

app = FastAPI()

# Serve static files. This makes the frontend and its assets accessible.
app.mount("/static", StaticFiles(directory="frontend"), name="static")

@app.get("/", response_class=HTMLResponse)
async def main():
    # Path to the index.html file
    index_html_path = os.path.join("frontend", "index.html")
    
    # Read and return the contents of the index.html file
    with open(index_html_path, 'r') as file:
        html_content = file.read()
    
    return HTMLResponse(content=html_content)
