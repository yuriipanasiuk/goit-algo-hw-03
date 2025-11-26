"""
Module for parsing user input commands.

Provides utility functions for command parsing and argument extraction.
"""

from decorators.input_error import input_error


@input_error
def parse_input(user_input: str):
    """Parse user input into a command and its arguments."""
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()

    return cmd, *args
