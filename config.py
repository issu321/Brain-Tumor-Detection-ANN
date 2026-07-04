import os
from datetime import timedelta

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'brain-tumor-detection-secret-key-2024'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///site.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    UPLOAD_FOLDER = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'static', 'uploads')
    MAX_CONTENT_LENGTH = 16 * 1024 * 1024  # 16MB max file size
    ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif', 'bmp', 'tiff'}
    REMEMBER_COOKIE_DURATION = timedelta(days=7)
    REMEMBER_COOKIE_SECURE = False
    SESSION_TYPE = 'filesystem'
    PERMANENT_SESSION_LIFETIME = timedelta(hours=2)

    # Branding Config
    BRAND_NAME = "Brain Tumor Detection Using ANN"
    BRAND_TAGLINE = "AI-Powered Medical Diagnosis System"
    GITHUB_USERNAME = "issu321"
    AUTHOR_NAME = "Mohammed Usman"
    GITHUB_REPO = "https://github.com/issu321/Brain-Tumor-Detection-ANN"
    CONTACT_EMAIL = "jaafreeusman@gmail.com"
    CONTACT_PHONE = "+91 8884294749"
    VERSION = "2.0.0"
