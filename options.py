from enum import Enum
class Options(Enum):
    VERBOSE = '--verbose'
    VERSION = '--version'
    WITH_CASES = '--with-cases'
    INTERPRETER = '--i'

    def __str__(self):
        return self.value
