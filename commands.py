from enum import Enum
class Commands(Enum):
    ADD = 'add'
    RUN = 'run'
    PASSING = 'passing'
    ATTEST = 'attest'

    def __str__(self):
        return self.value
