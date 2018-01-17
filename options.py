from enum import Enum
class Options(Enum):
    VERBOSE = '--verbose'
    VERSION = '--version'
    WITH_CASES = '--with-cases'

    def __str__(self):
        return self.value
