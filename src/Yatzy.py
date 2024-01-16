from src.Pips import Pips

class Yatzy:

    FIFTEEN = 15
    TWENTY = 20
    FIFTY = 50
    ZERO = 0

    def __init__(self, *dice):
        self.dice = list(dice)
    

    @classmethod
    def __count_num_x_num(cls, dice, num):
        return dice.count(num) * num
    
    @classmethod
    def __calc_pip_x_num(cls, group, num):
        """
            Cambio por map
        """
        return sum(map(lambda x: x * num, group))


    @classmethod
    def __filter_num_of_times(cls, dice, num):
        return set(filter(lambda x: dice.count(x) >= num, Pips.values()))
    

    @classmethod
    def __low_pair(cls, *dice):
        TWO = Pips.TWO
        pair = set(filter(lambda x: dice.count(x) == Pips.TWO, dice))
        return sum(value * TWO for value in pair) if pair else Yatzy.ZERO
    

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
        return cls.__count_num_x_num(dice, Pips.ONE)
    

    @classmethod
    def twos(cls, *dice):
        return cls.__count_num_x_num(dice, Pips.TWO)


    @classmethod
    def threes(cls, *dice):
        return cls.__count_num_x_num(dice, Pips.THREE)


    @classmethod
    def fours(cls, *dice):
        return cls.__count_num_x_num(dice, Pips.FOUR)


    @classmethod
    def fives(cls, *dice):
        return cls.__count_num_x_num(dice, Pips.FIVE)


    @classmethod
    def sixes(cls, *dice):
        return cls.__count_num_x_num(dice, Pips.SIX)


    @classmethod
    def score_pair(cls, *dice):
        """
            Sustitucion de metodo de filtracion por método de clase __filter_num_of_times
        """
        pair = cls.__filter_num_of_times(dice, Pips.TWO)
        return max(pair) * Pips.TWO if pair else Yatzy.ZERO
    

    @classmethod
    def two_pair(cls, *dice):
        pairs = cls.__filter_num_of_times(dice, Pips.TWO)
        
        if len(pairs) >= Pips.TWO:
            return cls.__calc_pip_x_num(pairs, Pips.TWO)
        return Yatzy.ZERO
    

    @classmethod
    def three_of_a_kind(cls, *dice):
        trio = cls.__filter_num_of_times(dice, Pips.THREE)
        return sum(value * Pips.THREE for value in trio) if trio else Yatzy.ZERO


    @classmethod
    def four_of_a_kind(cls, *dice):
        fours = cls.__filter_num_of_times(dice, Pips.FOUR)
        return sum(value * Pips.FOUR for value in fours) if fours else Yatzy.ZERO
        

    @staticmethod
    def smallStraight(*dice):
        values = Pips.values()
        return Yatzy.FIFTEEN if sorted(list(dice)) == values[:-1] else Yatzy.ZERO
    

    @staticmethod
    def largeStraight(*dice):
        values = Pips.values()
        return Yatzy.TWENTY if sorted(list(dice)) == values[1:] else Yatzy.ZERO
    

    @classmethod
    def fullHouse(cls, *dice):
        """
            Cambio en el algoritmo
        """
        if cls.__low_pair(*dice) and cls.three_of_a_kind(*dice):
            return Yatzy.__low_pair(*dice) + Yatzy.three_of_a_kind(*dice)
        return Yatzy.ZERO