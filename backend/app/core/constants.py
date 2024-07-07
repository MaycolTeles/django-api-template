"""
Module containing some constants for the django orm database and other settings.
"""

import os

from dotenv import load_dotenv


load_dotenv()


DB = os.getenv("DB")

DB_HOST = os.getenv("DB_HOST")

DB_USER = os.getenv("DB_USER")

DB_PASSWORD = os.getenv("DB_PASSWORD")

DB_PORT = os.getenv("DB_PORT")

DB_NAME = os.getenv("DB_NAME")

DJANGO_SECRET_KEY = os.getenv("DJANGO_SECRET_KEY")

DJANGO_ALLOWED_HOSTS = os.getenv("DJANGO_ALLOWED_HOSTS", "").split(" ")

DJANGO_CSRF_TRUSTED_ORIGINS = os.getenv("DJANGO_CSRF_TRUSTED_ORIGINS", "").split(" ")
