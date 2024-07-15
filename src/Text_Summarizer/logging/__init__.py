# THIS IS OUR CUSTOM LOGGER 

import os
import sys
import logging

logging_str = "[%(asctime)s: %(levelname)s: %(module)s: %(message)s]"
# asctime: The time when the log message was created.
# levelname: The level of the log message (e.g., INFO, DEBUG, ERROR).
# module: The module (filename) from which the log message was emitted.
# message: The actual log message.



log_dir = "logs"                                                    #  Specifies the directory named log
log_filepath = os.path.join(log_dir,"running_logs.log")             # Combines the directory path and the log file name to create the full path for the log file.
os.makedirs(log_dir, exist_ok=True)                                 # Creates the directory if it does not already exist.



logging.basicConfig(
    level= logging.INFO,                                            # Sets the logging level to INFO, which means that all messages at this level and above (INFO, WARNING, ERROR, CRITICAL) will be logged.
    format= logging_str,                                            # Specifies the format for the log messages (as defined earlier).

    handlers=[                                                      # Specifies where the log messages should be directed
        logging.FileHandler(log_filepath),                          # Logs messages to a file located at log_filepath.
        logging.StreamHandler(sys.stdout)                           # Logs messages to the standard output stream (typically the console).
    ]
)

logger = logging.getLogger("textSummarizerLogger")                  # Creates a logger object named "textSummarizerLogger". This logger can be used throughout the application to log messages.