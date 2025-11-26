"""
This module provides a function for displaying detailed log messages
for a given log level.
"""


def display_logs(logs: list, level: str):
    """Display detailed logs for a specific log level."""
    if len(logs) < 1:
        return print("[WARNING]: Logs list are empty")

    print(f"\nLog details for the level '{level.upper()}':")

    for log in logs:
        return print(f'{log['date']} {log["time"]} - {log["message"]}')
