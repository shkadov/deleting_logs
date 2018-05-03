#from config_file import file_ini, file_ini_check
#from check_path import check_path, log_path
#from remove_file import remove_file
from config_file import FileINICheck, file_ini
from check_path import CheckPath, log_path
from remove_file import FileRemove, log_path

def main():

    FileINICheck(file_ini)
    CheckPath(log_path)
    FileRemove(log_path)

if __name__ == '__main__':
    main()