from enum import Enum
class Commands(Enum):
    ADD = 'add'
    RUN = 'run'
    PASSING = 'passing'

    def __str__(self):
        return self.value
