from src.Pips import Pips

class Yatzy:

    FIFTEEN = 15
    TWENTY = 20
    FIFTY = 50
    ZERO = 0

    def __init__(self, *dice):
        self.dice = list(dice)
    

    @classmethod
    def __numCountXNum(cls, dice, num):
        return dice.count(num) * num
    

    @classmethod
    def __calcPipXNum(cls, group, num):
        """
            Cambio por map
        """
        return sum(map(lambda x: x * num, group))


    @classmethod
    def __filterNumOfTimes(cls, dice, num):
        return set(filter(lambda x: dice.count(x) >= num, Pips))
    

    @classmethod
    def __lowPair(cls, *dice):
        pair = set(filter(lambda x: dice.count(x) == Pips.TWO, dice))
        return cls.__calcPipXNum(pair, Pips.TWO) if pair else Yatzy.ZERO
    

    @staticmethod
    def chance(*dice):
        return sum(dice)


    @staticmethod
    def yatzy(*dice):
        return Yatzy.ZERO if dice.count(dice[0]) != 5 else Yatzy.FIFTY


    """
        Cambio en el metodo de calculo de las puntuaciones n a un metodo de clase
    """
    @classmethod
    def ones(cls, *dice):
        return cls.__numCountXNum(dice, Pips.ONE)
    

    @classmethod
    def twos(cls, *dice):
        return cls.__numCountXNum(dice, Pips.TWO)


    @classmethod
    def threes(cls, *dice):
        return cls.__numCountXNum(dice, Pips.THREE)


    @classmethod
    def fours(cls, *dice):
        return cls.__numCountXNum(dice, Pips.FOUR)


    @classmethod
    def fives(cls, *dice):
        return cls.__numCountXNum(dice, Pips.FIVE)


    @classmethod
    def sixes(cls, *dice):
        return cls.__numCountXNum(dice, Pips.SIX)


    @classmethod
    def scorePair(cls, *dice):
        """
            Sustitucion de metodo de filtracion por método de clase __filterNumOfTimes
        """
        pair = cls.__filterNumOfTimes(dice, Pips.TWO)
        return max(pair) * Pips.TWO if pair else Yatzy.ZERO
    

    @classmethod
    def twoPair(cls, *dice):
        pairs = cls.__filterNumOfTimes(dice, Pips.TWO)
        return cls.__calcPipXNum(pairs, Pips.TWO) if len(pairs) >= Pips.TWO else Yatzy.ZERO
        
    
    @classmethod
    def threeOfAKind(cls, *dice):
        trio = cls.__filterNumOfTimes(dice, Pips.THREE)
        return cls.__calcPipXNum(trio, Pips.THREE) if trio else Yatzy.ZERO


    @classmethod
    def fourOfAKind(cls, *dice):
        fours = cls.__filterNumOfTimes(dice, Pips.FOUR)
        return cls.__calcPipXNum(fours, Pips.FOUR) if fours else Yatzy.ZERO
        

    @staticmethod
    def smallStraight(*dice):
        values = list(Pips)
        return Yatzy.FIFTEEN if sorted(list(dice)) == values[:-1] else Yatzy.ZERO
    

    @staticmethod
    def largeStraight(*dice):
        values = list(Pips)
        return Yatzy.TWENTY if sorted(list(dice)) == values[1:] else Yatzy.ZERO
    

    @classmethod
    def fullHouse(cls, *dice):
        """
            Cambio en el algoritmo
        """
        if cls.__lowPair(*dice) and cls.threeOfAKind(*dice):
            return Yatzy.__lowPair(*dice) + Yatzy.threeOfAKind(*dice)
        return Yatzy.ZERO