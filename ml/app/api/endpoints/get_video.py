from fastapi import APIRouter, HTTPException
from fastapi.responses import FileResponse
import os

router = APIRouter()


@router.get("/video/{video_type}/{video_uuid}")
def get_video(video_type: str, video_uuid: str):
    if video_type not in ["original", "edited"]:
        raise HTTPException(status_code=400, detail="Invalid video type")

    video_path = f"app/temp/{video_type}/{video_uuid}/{video_type}.mp4"

    if not os.path.exists(video_path):
        raise HTTPException(status_code=404, detail="Video not found")

    filename = f"{video_type}.mp4"
    return FileResponse(video_path, media_type="video/mp4", filename=filename)
