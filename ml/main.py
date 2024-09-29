from fastapi import FastAPI
from app.api.endpoints import (get_video, video_processing, video_rerender, get_thumbnail)


app = FastAPI()

app.include_router(get_video.router)
app.include_router(video_processing.router)
app.include_router(video_rerender.router)
app.include_router(get_thumbnail.router)
