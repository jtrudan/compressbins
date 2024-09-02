from src.stringifybins import myfunctions

def test_stringify_bins():
    assert myfunctions.stringify_bins([0,2,4,6,8,10]) == ['0-2','2-4','4-6','6-8','8-10']