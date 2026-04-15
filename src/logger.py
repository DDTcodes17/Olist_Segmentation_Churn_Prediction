import os
import logging
from datetime import datetime

LOG_FILE = f"{datetime.now().strftime('%d_%m_%Y')}.log"

logs_path = os.path.join(os.getcwd(), "logs", datetime.now().strftime('%d_%m_%Y'))
os.makedirs(logs_path, exist_ok=True)

LOG_FILE_PATH = os.path.join(logs_path, LOG_FILE)
print(LOG_FILE_PATH)

logging.basicConfig(
    filename=LOG_FILE_PATH,
    format = "[ %(asctime)s ] %(linono)d %(name)s - %(levelname)s - %(message)s",
    level= logging.INFO
)


