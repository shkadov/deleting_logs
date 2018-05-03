import ConfigParser, os

file_ini = os.getcwd() + '/config.ini'


class FileINICheck:


    def __init__(self, file_ini):

        try:
            if os.path.exists(file_ini):
                return
            else:
                config = ConfigParser.ConfigParser()
                config.read(file_ini)
                config.add_section('vars')
                config.set('vars', 'log_path', '')
                config.set('vars', 'retention', '3')
                config.set('vars', 'logfile', '')
                config.add_section('S3')
                config.set('S3', 'username', '')
                config.set('S3', 'password', '')
                config.set('S3', 'bucket', '')
                config.set('S3', 'logpath', '')
                with open(file_ini, 'w') as f:
                    config.write(f)
                    f.close()

        except:
            return

    # file_ini_check(file_ini)
