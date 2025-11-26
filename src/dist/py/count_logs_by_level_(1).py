"""
This module provides a utility function for counting log entries
by their level.
"""

from collections import Counter


def count_logs_by_level(logs: list) -> dict:
    """Count the number of logs for each log level."""
    levels = [log["level"] for log in logs]
    count_logs = dict(Counter(levels))

    return count_logs
