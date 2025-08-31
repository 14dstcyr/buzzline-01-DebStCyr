"""
basic_consumer_stcyr.py

Custom consumer that reads the log file in real time
and raises alerts on specific conditions.
"""

import time
import re
from datetime import datetime
from utils.utils_logger import logger

# --------------------------------------------
# Define alert rules
# --------------------------------------------

# Simple pattern matches
ALERT_PATTERNS = [
    re.compile(r"status=freezer_failure"),
    re.compile(r"status=cancelled"),
]

# Temperature check (alert if temp_c >= 8)
TEMP_RE = re.compile(r"temp_c=(\d+)")

# Track last alert to avoid duplicates
last_alert = None


def analyze_and_alert(line: str):
    """Check a log line and raise alerts if rules are matched."""
    global last_alert

    # Get a timestamp for log readability
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Check simple alert patterns
    for pattern in ALERT_PATTERNS:
        if pattern.search(line):
            if last_alert != line:  # only log if it's not a duplicate
                logger.warning(f"ALERT [{timestamp}]: {line}")
                last_alert = line
            return

    # Check temperature threshold
    match = TEMP_RE.search(line)
    if match:
        temp = int(match.group(1))
        if temp >= 8:
            if last_alert != "temp":
                logger.warning(f"ALERT [{timestamp}]: {line}")
                last_alert = "temp"
            return

    # If no alert triggered, log as normal
    logger.info(f"OK [{timestamp}]: {line}")
    last_alert = None


def main():
    """Main consumer loop that tails the log file."""
    log_file = "logs/project_log.log"

    logger.info("START consumer...")
    try:
        with open(log_file, "r") as file:
            # Move to the end of file
            file.seek(0, 2)
            while True:
                line = file.readline()
                if not line:
                    time.sleep(1)
                    continue
                line = line.strip()
                if line:
                    analyze_and_alert(line)
    except KeyboardInterrupt:
        logger.info("Consumer stopped.")


if __name__ == "__main__":
    main()
