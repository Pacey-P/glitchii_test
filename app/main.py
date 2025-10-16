from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from app.routers import videos

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

app.include_router(videos.router)

@app.get("/")
async def read_index():
    return FileResponse('static/index.html')