import os
import sys
import logging
from datetime import datetime

# Setup
log_dir = "logs"
os.makedirs(log_dir, exist_ok=True)

# Create a log filename with a unique timestamp
timestamp = datetime.now().strftime('%Y_%m_%d-%H_%M_%S')
log_filename = f"{log_dir}/{timestamp}.log"

# Logging format and level
logging_str = "[%(asctime)s: %(levelname)s: %(module)s:%(lineno)d] %(message)s"
level = logging.INFO

# Create logger
logger = logging.getLogger("textSummarizerLogger")
logger.setLevel(level)

# File handler for writing logs to a file
file_handler = logging.FileHandler(log_filename)
file_handler.setFormatter(logging.Formatter(logging_str))
logger.addHandler(file_handler)

# Stream handler for printing logs to the console
stream_handler = logging.StreamHandler(sys.stdout)
stream_handler.setFormatter(logging.Formatter(logging_str))
logger.addHandler(stream_handler)
