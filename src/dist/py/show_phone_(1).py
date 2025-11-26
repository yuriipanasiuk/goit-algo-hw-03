"""
Module for managing contacts.

Provides functions for adding, changing, and retrieving contacts.
"""

from decorators.input_error import input_error


@input_error
def show_phone(args, contacts):
    """Return the phone number of a contact."""

    name = args[0]

    return f"{name}'s phone number is {contacts[name]}"
