from src.logger import logging
import sys
from src.exception import CustomException


logging.info('Hellow worlds')

try:
    a = 1 + "c"
except Exception as e:
    logging.info(CustomException(e,sys))
    raise CustomException(e, sys) from e 