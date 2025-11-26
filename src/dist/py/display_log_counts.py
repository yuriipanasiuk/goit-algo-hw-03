"""
This module provides a function to display a formatted summary
of log counts by their levels.
"""


def display_log_counts(counts: dict):
    """Display the number of log entries per level in a formatted table."""
    if not counts:
        return

    print("\nLogging level       Count")
    print("-----------------|----------")

    sorted_counts = sorted(counts.items(), key=lambda x: (-x[1], x[0]))

    for level, count in sorted_counts:
        print(f"{level:<16} | {count}")
