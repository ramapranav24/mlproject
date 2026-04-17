import logging
import os
from datetime import datetime

# create log file name
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

# create logs folder path (NOT including file name)
logs_dir = os.path.join(os.getcwd(), "logs")
os.makedirs(logs_dir, exist_ok=True)

# full file path
LOG_FILE_PATH = os.path.join(logs_dir, LOG_FILE)

# logging configuration
logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[%(asctime)s] [line:%(lineno)d] %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)

if __name__=="main":
    logging.info("LOgging gas started")