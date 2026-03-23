import os
from pathlib import Path

from dotenv import load_dotenv


load_dotenv()


class Config:
    BASE_DIR = Path(__file__).resolve().parent

    SECRET_KEY = os.getenv("SECRET_KEY", "dev")
    APP_NAME = os.getenv("APP_NAME", "Flask Skill App")
    FLASK_ENV = os.getenv("FLASK_ENV", "development")
    HOST = os.getenv("FLASK_HOST", "127.0.0.1")
    PORT = int(os.getenv("FLASK_PORT", "5000"))
    DEBUG = os.getenv("FLASK_DEBUG", "false").lower() == "true"
    SKILLS_DATA_FILE = os.getenv(
        "SKILLS_DATA_FILE",
        str(BASE_DIR / "data" / "skills.json"),
    )
