import logging
import os 
from datetime import datetime


#directory name
LOG_DIR = 'logs'

# making directorey 
os.makedirs(LOG_DIR, exist_ok=True)

#Creating timeframe for the log file
LOG_FILE_NAME = f"{datetime.now().strftime('%m_%d_%Y_%M_%H_%S')}.logs"


LOG_FILE_PATH = os.path.join(LOG_DIR, LOG_FILE_NAME)

logging.basicConfig(
    filename=LOG_FILE_PATH,
    format= '[%(asctime)s] %(name)s - %(lineno)d - %(levelname)s - %(message)s',
    level=logging.INFO,
)


"""
# other way is 


LOG_FILE = f"{datetime.now().strftime("%m_%d_%Y_%H_%M_%S")}.log"

logs_path = os.path.join(os.getcwd(), "logs", LOG_FILE)

os.makedirs(logs_path, exist_ok=True)

LOG_FILE_PATH = os.path.join(logs_path, LOG_FILE)
"""
