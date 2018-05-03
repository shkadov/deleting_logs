import os, ConfigParser, time, logging
from datetime import datetime
from config_file import file_ini


config = ConfigParser.ConfigParser()
config.read(file_ini)
log_path = config.get('vars', 'log_path')
retention = config.get('vars', 'retention')
logfile = config.get('vars', 'logfile')
current_time = time.time()
current_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

class FileRemove:
    def __init__ (self, log_path):
        global retention
        try:
            for dir, subdir, files in os.walk(log_path):
                for file in files:
                    file_name = os.path.join(dir, file)
                    file_date = os.path.getmtime(file_name)
                    file_age = (int(current_time) - int(file_date)) / 86400  # get current file age
                    retention = int(retention)
                    if file_age > retention:
                        with open(logfile, 'a') as f:
                            f.write(str(current_date) + ' File ' + str(file_name) + ' has been deleted (modify date: ' + str(datetime.fromtimestamp(file_date)) +' )\n')
                            f.close()
                        #os.remove(file_name)

        except BaseException as e:
            logging.error(str(e))

    #remove_file(log_path)