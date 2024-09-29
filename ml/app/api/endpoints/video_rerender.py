from fastapi import APIRouter, HTTPException, BackgroundTasks
from app.modules.video_rerender import VideoRerender

from app.utils.security_utils import verify_secret_token

router = APIRouter()


@router.post("/video-rerender/")
def video_processing(identity: str, uuid: str, transcription_raw: str, transcription_timecodes: str,fragment_title:str, secret_token: str,
                     background_tasks: BackgroundTasks):
    verify_secret_token(secret_token)

    video_rerender_task = VideoRerender(
        identity,
        uuid,
        transcription_raw,
        transcription_timecodes,
        fragment_title
    )
    background_tasks.add_task(video_rerender_task.start)

    return {"results": "Video rerender initiated"}

