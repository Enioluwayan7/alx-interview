#!/usr/bin/python3
import sys
import signal

# Initialize global variables for file size and status code counts
total_size = 0
status_codes_count = {code: 0 for code in [200, 301, 400, 401, 403, 404, 405, 500]}
line_count = 0

def print_stats():
    """Prints total file size and status code counts."""
    print(f"File size: {total_size}")
    for code in sorted(status_codes_count.keys()):
        if status_codes_count[code] > 0:
            print(f"{code}: {status_codes_count[code]}")

def process_line(line):
    """Processes a single line of input."""
    global total_size, status_codes_count, line_count
    try:
        parts = line.split()
        # Validate input format length and structure
        if len(parts) < 7:
            return

        # Extract file size and status code, validate they are integers
        status_code = int(parts[-2])
        file_size = int(parts[-1])

        # Add to total size
        total_size += file_size

        # Update status code count if it's one we're tracking
        if status_code in status_codes_count:
            status_codes_count[status_code] += 1

        line_count += 1
        if line_count % 10 == 0:
            print_stats()

    except (ValueError, IndexError):
        # Ignore lines that don't match the format
        pass

def signal_handler(sig, frame):
    """Handles keyboard interruption signal to print stats."""
    print_stats()
    sys.exit(0)

# Set up signal handler for keyboard interrupt
signal.signal(signal.SIGINT, signal_handler)

# Read standard input line by line
for line in sys.stdin:
    process_line(line.strip())
