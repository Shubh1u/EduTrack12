import os

class Config:
    # General settings
    SECRET_KEY = os.environ.get("SECRET_KEY", "supersecret")
    DEBUG = True

    # Database
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL", "sqlite:///edutrack.db")
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # JWT
    JWT_SECRET_KEY = os.environ.get("JWT_SECRET_KEY", "jwt-secret")

    # Optional: Uploads, Pagination, etc.
    MAX_CONTENT_LENGTH = 16 * 1024 * 1024  # 16MB upload limit
    ITEMS_PER_PAGE = 20
