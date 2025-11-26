"""
This module provides a function to filter log entries by their log level.
"""


def filter_logs_by_level(logs: list, level: str) -> list:
    """Filter logs by the specified log level."""

    filtered_logs = list(
        filter(lambda log: log["level"].upper() == level.upper(), logs)
    )

    return filtered_logs
