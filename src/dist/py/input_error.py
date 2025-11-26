"""
This module provides a decorator `input_error` to catch common input-related
errors (ValueError, KeyError, IndexError) and return user-friendly messages.
"""


def input_error(func):
    """
    Decorator to handle common input-related errors for functions.
    """

    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Give me name and phone please."
        except KeyError:
            return "Enter correct name."
        except IndexError:
            return "Not enough arguments. Please provide required data."

    return inner
