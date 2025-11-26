"""
This module provides utility functions for parsing and processing log files.
"""


def parse_log_line(line: str) -> dict:
    """Parse a single log line into a structured dictionary."""
    try:
        date, time, status, message = line.strip().split(maxsplit=3)

        result = {
            "date": date,
            "time": time,
            "level": status,
            "message": message,
        }

        return result

    except ValueError:
        return None
