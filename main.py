from config_file import file_ini, file_ini_check
from check_path import check_path, log_path
from remove_file import remove_file


def main():
    file_ini_check(file_ini)
    check_path(log_path)
    remove_file(log_path)

if __name__ == '__main__':
    main()