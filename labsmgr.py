from abc import ABC
import logging
import os

DEFAULT_LOG_LEVEL = 'INFO'
DEFAULT_LOG_FORMAT = '%(asctime)-15s %(levelname)-8s %(message)s'
DEFAULT_LOG_DATE_FORMAT = '%m-%d-%Y %H:%M:%S'

loglevel = os.getenv('LOG_LEVEL', DEFAULT_LOG_LEVEL)
numeric_level = getattr(logging, loglevel.upper(), None)

logging.basicConfig(format=DEFAULT_LOG_FORMAT, datefmt=DEFAULT_LOG_DATE_FORMAT, level=numeric_level)
print("Initializing Logger wit LogLevel: %s" % loglevel.upper())

