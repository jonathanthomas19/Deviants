
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

app = FastAPI()

# Serving static files from the "frontend" directory under "/static"
app.mount("/static", StaticFiles(directory="frontend"), name="static")

@app.get("/")
async def main():
    return {"message": "Welcome to Velocity Kingdom - A Racing Culture Exploration"}
