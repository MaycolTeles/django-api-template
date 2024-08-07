"""
Module to export management commands for the account app.

This module exports all the management commands available in the account app.
"""

__all__ = [
    "setup_user",
]


from .commands import setup_user
