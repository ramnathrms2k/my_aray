from .. import Array
import statistics

arr = Array([2, 3, 5, 4, 7, -8, 9, 10, -7])

def test_sum():
    assert arr.sum() == 25

def test_min():
    assert arr.min() == -8

def test_max():
    assert arr.max() == 10

def test_mean():
    assert arr.mean() == statistics.mean(arr.data)

def test_median():
    assert arr.median() == statistics.median(arr.data)
