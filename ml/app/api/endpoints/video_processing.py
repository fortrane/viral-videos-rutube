from fastapi import APIRouter, HTTPException, BackgroundTasks
from app.modules.video_processing import VideoProcessing

from app.utils.security_utils import verify_secret_token
import app.utils.cadri as cd
router = APIRouter()
import app.utils.main as mn

@router.post("/video-processing/")
def video_processing(identity: str, original_video: str, secret_token: str, add_soap_video: str, background_tasks: BackgroundTasks):
    verify_secret_token(secret_token)

    video_processing_task = VideoProcessing(
        identity,
        original_video,
        add_soap_video,
    )
    background_tasks.add_task(video_processing_task.start)

    return {"results": "Video processing initiated"}

