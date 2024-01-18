from enum import Enum


class ValueEnum(Enum):
    @classmethod
    def get_member(cls, name):
        return cls[name].value
