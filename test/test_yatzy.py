from src.Yatzy import Yatzy as yt

def test_chance_scores_sum_of_all_dice():
        expected = 15
        actual = yt.chance(2,3,4,5,1)
        assert expected == actual
        assert 16 == yt.chance(3,3,4,5,1)
  

def test_yatzy_scores_50():
        expected = 50
        actual = yt.yatzy(4,4,4,4,4)
        assert expected == actual
        assert 50 == yt.yatzy(6,6,6,6,6)
        assert 0 == yt.yatzy(6,6,6,6,3)
  

def test_1s():
        assert yt.ones(1,2,3,4,5) == 1
        assert 2 == yt.ones(1,2,1,4,5)
        assert 0 == yt.ones(6,2,2,4,5)
        assert 4 == yt.ones(1,2,1,1,1)
  

def test_2s():
        assert 4 == yt.twos(1,2,3,2,6)
        assert 10 == yt.twos(2,2,2,2,2)
  

def test_threes():
        assert 6 == yt.threes(1,2,3,2,3)
        assert 12 == yt.threes(2,3,3,3,3)
  

def test_fours_test():
        assert 12 == yt.fours(4,4,4,5,5)
        assert 8 == yt.fours(4,4,5,5,5)
        assert 4 == yt.fours(4,5,5,5,5)
  

def test_fives():
        assert 10 == yt.fives(4,4,4,5,5)
        assert 15 == yt.fives(4,4,5,5,5)
        assert 20 == yt.fives(4,5,5,5,5)
  

def test_sixes_test():
        assert 0 == yt.sixes(4,4,4,5,5)
        assert 6 == yt.sixes(4,4,6,5,5)
        assert 18 == yt.sixes(6,5,6,6,5)
  

def test_one_pair():
        assert 6 == yt.scorePair(3,4,3,5,6)
        assert 10 == yt.scorePair(5,3,3,3,5)
        assert 12 == yt.scorePair(5,3,6,6,5)
        assert 12 == yt.scorePair(6,6,6,6,5)
        assert 6 == yt.scorePair(2,2,3,3,5)
  

def test_twoPair():
        assert 16 == yt.twoPair(3,3,5,4,5)
        assert 18 == yt.twoPair(3,3,6,6,6)
        assert 0 == yt.twoPair(3,3,6,5,4)
  

def test_three_of_a_kind():
        assert 9 == yt.threeOfAKind(3,3,3,4,5)
        assert 15 == yt.threeOfAKind(5,3,5,4,5)
        assert 9 == yt.threeOfAKind(3,3,3,3,5)


def test_four_of_a_knd():
        assert 12 == yt.fourOfAKind(3,3,3,3,5)
        assert 20 == yt.fourOfAKind(5,5,5,4,5)
        assert 12 == yt.fourOfAKind(3,3,3,3,3)
        assert 0  == yt.fourOfAKind(3,3,3,2,1)
  

def test_smallStraight():
        assert 15 == yt.smallStraight(1,2,3,4,5)
        assert 15 == yt.smallStraight(2,3,4,5,1)
        assert 0 == yt.smallStraight(1,2,2,4,5)
  

def test_largeStraight():
        assert 20 == yt.largeStraight(6,2,3,4,5)
        assert 20 == yt.largeStraight(2,3,4,5,6)
        assert 0 == yt.largeStraight(1,2,2,4,5)
        assert 0 == yt.largeStraight(1,3,2,4,5)
  

def test_fullHouse():
        assert 18 == yt.fullHouse(6,2,2,2,6)
        assert 0 == yt.fullHouse(2,3,4,5,6)