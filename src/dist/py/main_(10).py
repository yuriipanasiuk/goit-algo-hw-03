"""
This module provides a command-line tool for analyzing log files.
"""

import sys
from helpers import (
    load_logs,
    display_log_counts,
    count_logs_by_level,
    filter_logs_by_level,
    display_logs,
)

VALID_LEVELS = ["INFO", "DEBUG", "ERROR", "WARNING"]


def main():
    """Main entry point for the log analyzer script."""
    if len(sys.argv) < 2:
        print("[ERROR] You must pass a directory path!")
        print("[INFO] Example: python hw03.py /path/to/logfile.log")
        print(
            "[INFO] Example: python hw03.py /path/to/logfile.log info | debug | error | warning"
        )
        sys.exit(1)

    # The first argument after the script name is the path to the log file
    logfile_path = sys.argv[1]

    # Load all logs from the specified file
    all_logs = load_logs(logfile_path)

    # Count the number of logs by their level (INFO, ERROR, etc.)
    logs_count = count_logs_by_level(all_logs)

    # Display a summary of log counts per level
    display_log_counts(logs_count)

    if len(sys.argv) >= 3:
        log_level_input = sys.argv[2].upper()

        # Check if the provided log level is valid
        if log_level_input not in VALID_LEVELS:
            print(
                f"\n[ERROR] Invalid log level '{sys.argv[2]}'. Must be one of: {', '.join([lvl.lower() for lvl in VALID_LEVELS])}"
            )
            sys.exit(1)

        # Filter logs by the given level
        filtered_logs = filter_logs_by_level(all_logs, log_level_input)

        # Display the filtered logs for the selected level
        display_logs(filtered_logs, log_level_input)


if __name__ == "__main__":
    main()
