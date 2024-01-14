from enum import IntEnum, unique

@unique
class Pips(IntEnum):
    ONE, TWO, THREE, FOUR, FIVE, SIX = range(1,7)