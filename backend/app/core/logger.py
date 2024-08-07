"""
Module to provide a single point of access to the logger.

This module is used to provide a single point of access to the logger.
This is done to ensure that the logger is always instantiated with the same configuration,
such as the component and subcomponent names.
"""

from structlog import stdlib


def get_logger(component: str, subcomponent: str, **kwargs) -> stdlib.BoundLogger:
    """
    Get the logger instance.

    This method returns the logger instance with the provided component and subcomponent names.

    Args:
    ----
    * `component` : `str`
        The name of the component.
    * `subcomponent` : `str`
        The name of the subcomponent.
    * `**kwargs` : `Any`
        Any additional keyword arguments to be passed to the logger.

    Returns:
    --------------
    `BoundLogger`
        The logger instance with the provided component and subcomponent names
        and any additional keyword arguments.
    """
    return stdlib.get_logger(component=component, subcomponent=subcomponent, **kwargs)
