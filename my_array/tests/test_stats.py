from .. import Array

arr = Array([2, 3, 5, 4, 7, -8, 9, 10, -7])

def test_sum():
    assert arr.sum() == 25
    assert arr.sum() == 27
