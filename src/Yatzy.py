from src.Pips import Pips

class Yatzy:

    FIFTEEN = 15
    TWENTY = 20
    FIFTY = 50
    ZERO = 0


    def __init__(self, *dice):
        self.dice = list(dice)


    @staticmethod
    def chance(*dice):
        return sum(dice)


    @staticmethod
    def yatzy(*dice):
        return Yatzy.ZERO if dice.count(dice[0]) != 5 else Yatzy.FIFTY


    @staticmethod
    def ones(*dice):
        return dice.count(Pips.ONE) * Pips.ONE

    
    @staticmethod
    def twos(*dice):
        return dice.count(Pips.TWO) * Pips.TWO


    @staticmethod
    def threes(*dice):
        return dice.count(Pips.THREE) * Pips.THREE


    @staticmethod
    def fours(*dice):
        return dice.count(Pips.FOUR) * Pips.FOUR


    @staticmethod
    def fives(*dice):
        return dice.count(Pips.FIVE) * Pips.FIVE
    

    @staticmethod
    def sixes(*dice):
        return dice.count(Pips.SIX) * Pips.SIX


    @staticmethod
    def score_pair(*dice):
        """
            Use filter and lambda
        """
        pair = set(filter(lambda x: dice.count(x) >= Pips.TWO, dice))
        return max(pair) * Pips.TWO if pair else Yatzy.ZERO


    @staticmethod
    def two_pair(*dice):
        """
            Use filter and lambda
        """
        pairs = set(filter(lambda x: dice.count(x) >= Pips.TWO, dice))
        return sum(value * Pips.TWO for value in pairs) if len(pairs) >= Pips.TWO else Yatzy.ZERO
    
    @staticmethod
    def three_of_a_kind(*dice):
        THREE = Pips.THREE
        trio = {num for num in Pips.values() if dice.count(num) >= THREE}
        return sum(value * THREE for value in trio) if trio else Yatzy.ZERO


    @staticmethod
    def four_of_a_kind(*dice):
        FOUR = Pips.FOUR
        fours = {num for num in Pips.values() if dice.count(num) >= FOUR}
        return sum(value * FOUR for value in fours) if fours else Yatzy.ZERO
        

    @staticmethod
    def smallStraight(*dice):
        values = Pips.values()
        return Yatzy.FIFTEEN if sorted(list(dice)) == values[:-1] else Yatzy.ZERO
    

    @staticmethod
    def largeStraight(*dice):
        values = Pips.values()
        return Yatzy.TWENTY if sorted(list(dice)) == values[1:] else Yatzy.ZERO
    

    @staticmethod
    def fullHouse(*dice):
        PAIR = Pips.TWO
        TRIO = Pips.THREE
        full = {
            'pair': 0,
            'trio': 0
        }

        for num in Pips.values():
            if dice.count(num) == PAIR:
                full['pair'] = num 
            elif dice.count(num) == TRIO:
                full['trio'] = num
            
        if full.values() != 0:
            return full['pair'] * 2 + full['trio'] * 3
        return Yatzy.ZERO
