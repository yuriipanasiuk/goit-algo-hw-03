"""
This module provides a function to load and parse log entries from a file.
"""

from helpers.parse_log_line import parse_log_line


def load_logs(file_path: str) -> list:
    """Load logs from a file and parse each line into
    a structured dictionary.
    """
    logs = []

    try:
        with open(file_path, encoding="utf-8") as f:

            for line in f:
                parsed_log = parse_log_line(line)

                if parsed_log:
                    logs.append(parsed_log)
                else:
                    print(f"[Error]: Failed to parse log {line.strip()}")

            return logs

    except FileNotFoundError:
        print(f"[Error]: File path '{file_path}' not found")
        return []

    except (IOError, OSError) as e:
        print(f"[Error]: An error occurred while reading the file: {e}")
        return []
