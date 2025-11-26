"""
Module for managing contacts.

Provides functions for adding, changing, and retrieving contacts.
"""

from decorators.input_error import input_error


@input_error
def add_contact(args, contacts):
    """Add a new contact to the contacts dictionary."""

    name, phone = args
    contacts[name] = phone

    return "Contact added."
