"""
Module to define the task to setup a user.

This module defines a function to setup a user.
This function can be run synchronously as a normal function or asynchronously as a Celery task.
"""

from celery import shared_task

from account.models import User
from core.logger import get_logger


logger = get_logger(component="account", subcomponent="tasks", task="task_setup_user")


@shared_task
def task_setup_user(user_id: str) -> None:
    """
    Task to setup a user by creating the necessary setups.

    This task will setup a user by creating the necessary setups.
    This task can be run synchronously as a normal function or asynchronously as a Celery task.

    Args:
    ----
    * `user_id` : `str`
        The id of the user to be set up.
    """
    logger.info('task "task_setup_user" started')

    try:
        user = User.objects.get(id=user_id)
        logger.info("Setting user up", user=user)
        # SETUP THE USER HERE

    except Exception as e:
        logger.exception("An error occurred while setting the user up", user_id=user_id, error=e)

    logger.info('task "task_setup_user" finished')
