from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.responses import RedirectResponse

app = FastAPI()

# Serve static files. This makes the frontend and its assets accessible.
app.mount("/static", StaticFiles(directory="frontend"), name="static")

@app.get("/")
async def main():
    # Redirect to the index.html page served under /static
    return RedirectResponse(url="/static/index.html")
