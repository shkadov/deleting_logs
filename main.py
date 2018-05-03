import os, time, logging

from datetime import datetime


logs_path = ''
logfile   = os.getcwd() + '/retention_log.txt'
retention = 32
current_time = time.time()
current_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

def check_path(logs_path):
    try:
        if not os.path.exists(logs_path):
            print("Path is not found")
    except:
        return


def remove_file(logs_path):
    try:
        for dir, subdir, files in os.walk(logs_path):
            for file in files:
                file_name = os.path.join(dir, file)
                file_date = os.path.getmtime(file_name)
                file_age = (int(current_time) - int(file_date)) / 86400  # get current file age
                if file_age > retention:
                    with open(logfile, 'a') as f:
                        f.write(str(current_date) + ' File ' + str(file_name) + ' has been deleted (modify date: ' + str(datetime.fromtimestamp(file_date)) +' )\n')
                        f.close()
                    #os.remove(file_name)

    except BaseException as e:
        logging.error(str(e))

def main():
    check_path(logs_path)
    remove_file(logs_path)

if __name__ == '__main__':
    main()