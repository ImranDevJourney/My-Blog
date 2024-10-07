import os


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'a_default_secret_key'  # Change this in production
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///site.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # Optional: Configure mail settings if you plan to send emails (e.g., for password resets)
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')

    # Additional configuration options can be added here