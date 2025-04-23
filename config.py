from pydantic_settings import BaseSettings
from typing import Literal


class Settings(BaseSettings):
    # BrowserStack credentials
    browserstack_username: str
    browserstack_access_key: str
    browserstack_url: str

    # Android Configuration
    android_platform_version: str
    android_device_name: str
    android_app: str

    # iOS Configuration
    ios_platform_version: str
    ios_device_name: str
    ios_app: str

    # Common Configuration
    project_name: str
    build_name: str
    session_name: str

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


config = Settings() 