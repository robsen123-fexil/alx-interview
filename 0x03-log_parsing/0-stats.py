#!/usr/bin/python3
"""
Script for parsing logs and computing metrics
"""

import sys
import re


def display_metrics(log: dict) -> None:
    """
    Display the accumulated metrics: total file size and status code counts.
    """
    print(f"File size: {log['file_size']}")
    for code in sorted(log['code_frequency']):
        if log['code_frequency'][code] > 0:
            print(f"{code}: {log['code_frequency'][code]}")


if __name__ == "__main__":
    # Regex pattern to match the expected log format
    log_pattern = re.compile(
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3} - \[\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}.\d+\] "GET /projects/260 HTTP/1.1" (\d{3}) (\d+)'
    )

    line_counter = 0
    log_data = {"file_size": 0, "code_frequency": {str(code): 0 for code in [200, 301, 400, 401, 403, 404, 405, 500]}}

    try:
        # Read from standard input
        for line in sys.stdin:
            line = line.strip()
            match = log_pattern.fullmatch(line)
            if match:
                line_counter += 1
                status_code = match.group(1)
                file_size = int(match.group(2))

                # Update total file size
                log_data["file_size"] += file_size

                # Update the count for the status code
                if status_code.isdigit():
                    log_data["code_frequency"][status_code] += 1

                # Output metrics every 10 lines
                if line_counter % 10 == 0:
                    display_metrics(log_data)
    finally:
        # Ensure metrics are displayed at the end
        display_metrics(log_data)
