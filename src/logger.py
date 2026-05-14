import logging
import os
from datetime import datetime

LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log" #creates a unique filename based on current date and time
logs_path = os.path.join(os.getcwd(), "logs", LOG_FILE) #builds the folder path where log file will live
os.makedirs(logs_path, exist_ok = True) #create folder, if folder already exists — don't crash, just continue
LOG_FILE_PATH = os.path.join(logs_path, LOG_FILE) #Builds the full path to the actual log file

logging.basicConfig(
    filename = LOG_FILE_PATH,
    format = "[%(asctime)s] %(lineno)d %(name)s - %(levelname)s -%(message)s",
    level = logging.INFO,
)

# if __name__ == "__main__":
#     logging.info("Logging has started")