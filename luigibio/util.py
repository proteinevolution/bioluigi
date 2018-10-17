"""
Utilities for the Luigi Biopython Extension

@author Lukas Zimmermann
"""


def value_error_if(test: bool, message: str):
    """
    Raises :py:class:`~ValueError` if the test is true
    :param test: The test which determines whether value error will be raised
    :param message: The message the ValueError will be associated with
    """
    if test:
        raise ValueError(message)
