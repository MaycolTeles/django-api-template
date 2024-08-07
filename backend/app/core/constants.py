"""
Module containing some constants for the django orm database and other settings.
"""

from decouple import config


def _split_env_string(env_string: str) -> list[str]:
    """
    Parse a string from the environment into a list.

    Example:
    ----------
    `"localhost 127.0.0.1 0.0.0.0"` -> [`"localhost"`, `"127.0.0.1"`, `"0.0.0.0"`]

    Args:
    ----
    * `env_string`: `str`
        The string to be parsed.
    """
    return env_string.split(" ")


DB = config("DB")

DB_HOST = config("DB_HOST")

DB_USER = config("DB_USER")

DB_PASSWORD = config("DB_PASSWORD")

DB_PORT = config("DB_PORT")

DB_NAME = config("DB_NAME")

DJANGO_SECRET_KEY = config("DJANGO_SECRET_KEY")

DJANGO_DEBUG = config("DJANGO_DEBUG", cast=bool, default=False)

DJANGO_ALLOWED_HOSTS: list[str] = config("DJANGO_ALLOWED_HOSTS", cast=_split_env_string)  # type: ignore

DJANGO_CSRF_TRUSTED_ORIGINS: list[str] = config("DJANGO_CSRF_TRUSTED_ORIGINS", cast=_split_env_string)  # type: ignore
