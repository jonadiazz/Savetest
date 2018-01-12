from enum import Enum
class GlobalVars(Enum):
    SAVED_TESTS = '.savedtests.'
    JSON =  '.json'

    def __str__(self):
        return self.value
