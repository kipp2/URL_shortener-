import os 
from flask_sqlalchemy import SQLAlchemy

class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL", "postgresql://ray:123456@localhost/url_shortener")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.getenv("SECRET_KEY", "supersecretkey")
