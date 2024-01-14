from src.Pips import Pips

class Yatzy:

    FIFTY = 50
    ZERO = 0

    def __init__(self, *dice):
        self.dice = list(dice)


    @staticmethod
    def chance(*dice):
        return sum(num for num in dice)


    @staticmethod
    def yatzy(dice):
        if dice.count(dice[0]) != 5:
            return Yatzy.ZERO
        return 50

    ones = lambda *dice : dice.count(Pips.ONE) * Pips.ONE

    
    @staticmethod
    def twos(*dice):
        TWO = Pips.TWO
        return dice.count(TWO) * TWO


    @staticmethod
    def threes(*dice):
        THREE = Pips.THREE
        return dice.count(THREE) * THREE


    def fours(self):
        FOUR = Pips.FOUR
        return self.dice.count(FOUR) * FOUR


    def fives(self):
        FIVE = Pips.FIVE
        return self.dice.count(FIVE) * FIVE
    

    def sixes(self):
        SIX = Pips.SIX
        return self.dice.count(SIX) * SIX
    

    @staticmethod
    def score_pair(*dice):
        PAIR = Pips.TWO
        pair = {num for num in Pips.values() if dice.count(num) >= PAIR}
        return max(pair) * PAIR if pair else Yatzy.ZERO


    @staticmethod
    def two_pair(*dice):
        PAIR = Pips.TWO
        pairs = {num for num in Pips.values() if dice.count(num) >= PAIR}
        return sum(value * PAIR for value in pairs) if len(pairs) >= PAIR else Yatzy.ZERO
        

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
        throw = list(dice)
        possible_straight = list(range(1, 6))
        
        if sorted(throw) == possible_straight:
            return 15
        return Yatzy.ZERO
    

    @staticmethod
    def largeStraight(*dice):
        throw = list(dice)
        possible_straight =  list(range(2, 7))

        if sorted(throw) == possible_straight:
            return 20
        return Yatzy.ZERO
    

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