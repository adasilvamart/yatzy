from src.Pips import Pips

def test_pips_representation():

    assert Pips.ONE == 1
    assert Pips.TWO == 2
    assert Pips.THREE == 3
    assert Pips.FOUR == 4
    assert Pips.FIVE == 5
    assert Pips.SIX == 6


def test_pips_operations():
    assert Pips.FOUR ==  Pips.ONE + Pips.THREE
    assert Pips.SIX == Pips.ONE + Pips.FIVE
    assert Pips.TWO == Pips.SIX - Pips.FOUR
    assert 0 == Pips.FOUR - Pips.FOUR