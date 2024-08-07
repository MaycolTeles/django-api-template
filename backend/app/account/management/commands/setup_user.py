"""
Module containing the command to setup a user.
"""

import djclick as click

from account.tasks import task_setup_user
from core.logger import get_logger


logger = get_logger(component="account", subcomponent="commands", command="setup_user")


@click.command()
@click.argument("user_id")
def setup_user(user_id: str) -> None:
    """
    Command to setup a user.

    This command will setup a user asynchronously by calling the `task_setup_user` task
    and adding it to the Celery task queue using the `delay` method.

    To run this command, run the following command:

    ```bash
    python manage.py setup_user <user_id>
    ```

    For example:

    ```bash
    python manage.py setup_user 12345678-1234-1234-1234-123456789012
    ```

    Args:
    ----
    * `user_id` : `str`
        The id of the user to be set up.
    """
    logger.info("Setting user up", user_id=user_id)

    try:
        task_setup_user.delay(user_id)

    except Exception as e:
        logger.exception("An error occurred while setting the user up", user_id=user_id, error=e)
