from enum import IntEnum, unique

@unique
class Pips(IntEnum):
    ONE, TWO, THREE, FOUR, FIVE, SIX = range(1,7)

    @classmethod
    def values(cls):
        return [num._value_ for num in Pips.__members__.values()]