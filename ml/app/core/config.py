from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    API_SECRET_TOKEN: str = "SECRET_KEY"
    API_LINK: str = "http://127.0.0.1/src/Api/v1.external.php?"
    SERVER_LINK: str = "http://127.0.0.1/"

    class Config:
        env_file = ".env"


settings = Settings()
