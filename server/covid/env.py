import platform
import enum
import os
import sys

# setup logging configuration
module_path = os.path.dirname(__file__)
project_root_dir_path = os.path.dirname(module_path)
log_dir = os.path.join(project_root_dir_path, 'data', 'logs')

# add the oildb module to sys path
sys.path.append(module_path)


def detect_environment():
    system = platform.system()
    if system == 'Windows':
        return EnvironmentType.DEV_LOCAL
    else:
        return EnvironmentType.DEV_SERVER


class EnvironmentType(enum.Enum):
    DEV_LOCAL = ('sqlite:///C:\\code\\DB\\data\\mydb.db', True)
    DEV_SERVER = ('postgresql://xyz:abc@localhost/123', False)

    def __init__(self, db_uri, debug):
        self.database_uri = db_uri
        self.debug = debug

    @property
    def secret_key(self):
        return '123456789abcdefg'

    @property
    def logs_filename(self):
        return log_dir + os.path.sep + "covid_logs.log"

