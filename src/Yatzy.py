class Yatzy:

    def __init__(self, *dice):
        self.dice = list(dice)


    @staticmethod
    def chance(*dice):
        score = 0
        for num in dice:
            score += num
        return score


    @staticmethod
    def yatzy(dice):
        if dice.count(dice[0]) != 5:
            return 0
        return 50


    @staticmethod
    def ones(*dice):
        ONE = 1
        return dice.count(ONE)
    

    @staticmethod
    def twos(*dice):
        TWO = 2
        return dice.count(TWO) * TWO


    @staticmethod
    def threes(*dice):
        THREE = 3
        return dice.count(THREE) * THREE


    def fours(self):
        FOUR = 4
        return self.dice.count(FOUR) * FOUR


    def fives(self):
        FIVE = 5
        return self.dice.count(FIVE) * FIVE
    

    def sixes(self):
        SIX = 6
        return self.dice.count(SIX) * SIX
    

    @staticmethod
    def score_pair(*dice):
        PAIR = 2
        pair = set()

        for num in range(6, 0, -1):
            if dice.count(num) >= PAIR:
                pair.add(num)
        
        if pair:
                return max(pair) * PAIR
        return 0
    

    @staticmethod
    def two_pair(*dice):
        PAIR = 2
        score = 0
        pairs = set()

        for num in range(6, 0, -1):
            if dice.count(num) >= PAIR:
                pairs.add(num)

        if len(pairs) == 2:
            for value in pairs:
                score += value * 2
            return score
        return 0

    @staticmethod
    def three_of_a_kind(*dice):
        THREE = 3
        trio = set()

        for num in range(6, 0, -1):
            if dice.count(num) >= THREE:
                trio.add(num)
        if trio:
            for value in trio:
                return value * THREE
        return 0

    @staticmethod
    def four_of_a_kind(*dice):
        FOUR = 4
        score = 0
        fours = set()

        for num in range(6, 0, -1):
            if dice.count(num) >= FOUR:
                fours.add(num)
        if fours:
            for value in fours:
                score += value * FOUR
            return score
        return 0


    @staticmethod
    def smallStraight(*dice):
        throw = list(dice)
        possible_straight = [1, 2, 3, 4, 5]
        
        if sorted(throw) == possible_straight:
            return 15
        return 0
    
    @staticmethod
    def largeStraight(*dice):
        throw = list(dice)
        possible_straight = [2, 3, 4, 5, 6]

        if sorted(throw) == possible_straight:
            return 20
        return 0
    
    
    @staticmethod
    def fullHouse(*dice):
        PAIR = 2
        TRIO = 3
        full = {
            'pair': 0,
            'trio': 0
        }

        for num in range (6, 0, -1):
            if dice.count(num) == PAIR:
                full['pair'] = num 
            elif dice.count(num) == TRIO:
                full['trio'] = num
            
        if full.values() != 0:
            return full['pair'] * 2 + full['trio'] * 3
        return 0
    
