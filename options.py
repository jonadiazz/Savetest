from enum import Enum
class Options(Enum):
    VERBOSE = '--verbose'
    VERSION = '--version'

    def __str__(self):
        return self.value
