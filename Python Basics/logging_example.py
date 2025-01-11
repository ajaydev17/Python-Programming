"""
The logging module in Python provides a flexible framework for outputting log messages
with different severity levels (DEBUG, INFO, WARNING, ERROR, CRITICAL). By setting up a
logger with levels and handlers, you can control the format and output of each message.
"""

import logging

# configure logging
logging.basicConfig(level=logging.INFO, filename='app.log', filemode='a', format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# logging messages with different levels
logging.debug('This is a debug message')
logging.info('This is an info message')
logging.warning('This is a warning message')
logging.error('This is an error message')
logging.critical('This is a critical message')

# Each message has a severity level, enabling selective filtering based on the desired logging detail
