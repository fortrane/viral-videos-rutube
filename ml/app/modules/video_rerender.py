import os
import json

import requests

import app.utils.main as fm
from app.core.config import settings

class VideoRerender:

    def __init__(self, identity: str, uuid: str, transcription_raw: str, transcription_timecodes: str, fragment_title: str):
        self.identity = identity
        self.uuid = uuid
        self.transcription_raw = transcription_raw
        self.transcription_timecodes = transcription_timecodes
        self.title = fragment_title

    def start(self):
        # send return data to API for updating

        rerendered_video_path = f"temp/edited/{self.uuid}/edited.mp4"
        data_video=fm.change_video(self.uuid,self.transcription_timecodes,self.title)
        rerendered_data = {
            "id": self.identity,
            "uuid": self.uuid,
            "status": "Completed",
            "video_link": f"{settings.SERVER_LINK}video/{data_video['resname']}"
        }

        self.update_api(rerendered_data)

    def update_api(self, data):
        response = requests.post(f"{settings.API_LINK}updateVideoFragment", data={
            "secret-key": settings.API_SECRET_TOKEN,
            **data
        })
        if response.status_code != 200:
            print(f"Failed to update API: {response.text}")
