from enum import Enum
class Commands(Enum):
    ADD = 'add'
    RUN = 'run'

    def __str__(self):
        return self.value
