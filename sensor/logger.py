import logging
import os
from datatime import datatime
import os

LOG_FILE_NAME = f"{datatime.now().strftime('%m%d%Y__%H%M%S')}.log"


LOG_FILE_DIR = os.path.join(os.getcwd(),"logs")

os.mkdir(LOG_FILE_DIR,exist_ok=True)



LOG_FILE_PATH = os.path.join(LOG_FILE_DIR,LOG_FILE_NAME)



logging.basicConfig(

    filename=LOG_FILE_PATH,
    format="[%(asctime)s ] %(lin"
)
