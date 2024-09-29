from fastapi import HTTPException
from app.core.config import settings


def verify_secret_token(secret_token: str):
    if secret_token != settings.API_SECRET_TOKEN:
        raise HTTPException(status_code=403, detail="Invalid secret token")
    return True