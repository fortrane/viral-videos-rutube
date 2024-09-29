from fastapi import APIRouter, HTTPException
from fastapi.responses import FileResponse
import os

router = APIRouter()


@router.get("/thumbnail/{thumbnail_uuid}")
def get_thumbnail(thumbnail_uuid: str):
    thumbnail_path = f"app/temp/thumbnails/{thumbnail_uuid}.png"

    if not os.path.exists(thumbnail_path):
        raise HTTPException(status_code=404, detail="Thumbnail not found")

    return FileResponse(thumbnail_path, media_type="image/png", filename=f"{thumbnail_uuid}.png")