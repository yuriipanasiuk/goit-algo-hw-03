"""
Module for managing contacts and displaying them.
"""


def show_all(contacts: dict) -> str:
    """Return all contacts as a formatted string."""

    if not contacts:
        return "Contacts list are empty"
    contact_list = [f"{name}: {phone}" for name, phone in contacts.items()]

    return "\n".join(contact_list)
