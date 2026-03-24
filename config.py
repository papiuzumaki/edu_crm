import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'edu-crm-secret-key-2024'
    DEBUG = True