"""
Module to export tasks for the account app.

This module exports all the tasks available in the account app.
The tasks are used to perform asynchronous operations but can also be used synchronously as normal functions.
"""

__all__ = [
    "task_setup_user",
]


from .setup_user import task_setup_user
