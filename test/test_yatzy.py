from src.Yatzy import Yatzy as yt

def test_chance_scores_sum_of_all_dice():
        expected = 15
        actual = yt.chance(2,3,4,5,1)
        assert expected == actual
        assert 16 == yt.chance(3,3,4,5,1)
  

def test_yatzy_scores_50():
        expected = 50
        actual = yt.yatzy([4,4,4,4,4])
        assert expected == actual
        assert 50 == yt.yatzy([6,6,6,6,6])
        assert 0 == yt.yatzy([6,6,6,6,3])
  

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
        assert 12 == yt(4,4,4,5,5).fours()
        assert 8 == yt(4,4,5,5,5).fours()
        assert 4 == yt(4,5,5,5,5).fours()
  

def test_fives():
        assert 10 == yt(4,4,4,5,5).fives()
        assert 15 == yt(4,4,5,5,5).fives()
        assert 20 == yt(4,5,5,5,5).fives()
  

def test_sixes_test():
        assert 0 == yt(4,4,4,5,5).sixes()
        assert 6 == yt(4,4,6,5,5).sixes()
        assert 18 == yt(6,5,6,6,5).sixes()
  

def test_one_pair():
        assert 6 == yt.score_pair(3,4,3,5,6)
        assert 10 == yt.score_pair(5,3,3,3,5)
        assert 12 == yt.score_pair(5,3,6,6,5)
        assert 12 == yt.score_pair(6,6,6,6,5)
        assert 6 == yt.score_pair(2,2,3,3,5)
  

def test_two_Pair():
        assert 16 == yt.two_pair(3,3,5,4,5)
        assert 18 == yt.two_pair(3,3,6,6,6)
        assert 0 == yt.two_pair(3,3,6,5,4)
  

def test_three_of_a_kind():
        assert 9 == yt.three_of_a_kind(3,3,3,4,5)
        assert 15 == yt.three_of_a_kind(5,3,5,4,5)
        assert 9 == yt.three_of_a_kind(3,3,3,3,5)
  

def test_four_of_a_knd():
        assert 12 == yt.four_of_a_kind(3,3,3,3,5)
        assert 20 == yt.four_of_a_kind(5,5,5,4,5)
        assert 12 == yt.four_of_a_kind(3,3,3,3,3)
        assert 0  == yt.four_of_a_kind(3,3,3,2,1)
  

def test_smallStraight():
        assert 15 == yt.smallStraight(1,2,3,4,5)
        assert 15 == yt.smallStraight(2,3,4,5,1)
        assert 0 == yt.smallStraight(1,2,2,4,5)
  

def test_largeStraight():
        assert 20 == yt.largeStraight(6,2,3,4,5)
        assert 20 == yt.largeStraight(2,3,4,5,6)
        assert 0 == yt.largeStraight(1,2,2,4,5)
  

def test_fullHouse():
        assert 18 == yt.fullHouse(6,2,2,2,6)
        assert 0 == yt.fullHouse(2,3,4,5,6)