import os, ConfigParser
from config_file import file_ini

config = ConfigParser.ConfigParser()
config.read(file_ini)
log_path = config.get('vars', 'log_path')

def check_path(log_path):
    try:
        if not os.path.exists(log_path):
            print("Path is not found")
    except:
        return

check_path(log_path)