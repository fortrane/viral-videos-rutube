import json
import uuid
import os

import requests
from app.core.config import settings

import app.utils.main as fm
class VideoProcessing:
    def __init__(self, identity: str, original_video: str,add_soap_video: str):
        self.identity = identity
        self.original_video = original_video
        self.soap = add_soap_video

    def start(self):
        # send return data to API for updating
        fragment_uuid = str(uuid.uuid4())
        video_path = f"app/temp/original/{self.identity}/"
        video_name = f"app/temp/original/{self.identity}/original.mp4"
        self.download_video(self.original_video,video_path,video_name)
        res_data=fm.find_moments(fragment_uuid,video_name,self.soap)

        processed_data = {
            "id": self.identity,
            "status": "Completed",
            "video_json": json.dumps(res_data[0]),
            "metric_score": json.dumps(res_data[1])
        }

        self.update_api(processed_data)

    def download_video(self,video_url, output_path, name):
        response = requests.get(video_url, stream=True)
        os.makedirs(output_path, exist_ok=True)
        if response.status_code == 200:
            with open(name, 'wb') as file:
                for chunk in response.iter_content(chunk_size=8192):
                    file.write(chunk)

        else:
            print(f"{response.status_code}")
    def update_api(self, data):
        response = requests.post(f"{settings.API_LINK}updateVideoData", data={
            "secret-key": settings.API_SECRET_TOKEN,
            **data
        })
        if response.status_code != 200:
            print(f"Failed to update API: {response.text}")
