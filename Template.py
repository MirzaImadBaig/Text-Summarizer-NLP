import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')
# Sets the logging level to INFO, meaning it will capture and display informational messages.

project_name = "Text_Summarizer"

list_of_files = [
    ".github/workflows/.gitkeep",                      # A placeholder file to ensure the workflows directory under .github is tracked by git. This is commonly used for CI/CD pipelines.
    f"src/{project_name}/__init__.py",                 # An initialization file for the Text_Summarizer package.      
    f"src/{project_name}/conponents/__init__.py",      # An initialization file for the components subpackage.
    f"src/{project_name}/utils/__init__.py",           # An initialization file for the utils subpackage.
    f"src/{project_name}/utils/common.py",             # A Python script for common utility functions.
    f"src/{project_name}/logging/__init__.py",         # An initialization file for the logging subpackage.
    f"src/{project_name}/config/__init__.py",          # An initialization file for the config subpackage.
    f"src/{project_name}/config/configuration.py",     # A Python script for configuration-related functionality.
    f"src/{project_name}/pipeline/__init__.py",        # An initialization file for the pipeline subpackage.
    f"src/{project_name}/entity/__init__.py",          # An initialization file for the entity subpackage.
    f"src/{project_name}/constants/__init__.py",       # An initialization file for the constants subpackage.
    "config/config.yaml", 
    "params.yaml",
    "app.py",
    "main.py",
    "Dockerfile",
    "requirements.txt", 
    "setup.py",                                       # A setup script for installing the project as a package.
    "research/trials.ipynb",                          # A Jupyter notebook for research and experimentation.
]

for filepath in list_of_files:
    filepath = Path(filepath)                                                          # Converts the string file path to a Path object for easier manipulation
    filedir, filename = os.path.split(filepath)                                        # Splits the path into the directory part (filedir) and the filename part (filename)

    if filedir != "":                                                                  # Creates the Directory if It Doesn't Exist
        os.makedirs(filedir, exist_ok=True)                                            # Creates the directory and check 'exist_ok=True' to avoid raising an error if the directory already exists
        logging.info(f"Creating directory:{filedir} for the file {filename}")          # Logs the creation of the directory

    
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):             # Checks if the file does not exist or if it exists but is empty (size is 0 bytes)
        with open(filepath,'w') as f:                                                  # Opens the file in write mode ('w'), which creates an empty file if it doesn't already exist, and then immediately closes it 
            pass
            logging.info(f"Creating empty file: {filepath}")                           # Logs the creation of the empty file.


    
    else:                                                                              # If the file already exists and is not empty, it logs that the file already exists
        logging.info(f"{filename} is already exists")