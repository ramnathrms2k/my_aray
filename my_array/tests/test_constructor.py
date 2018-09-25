from .. import Array

def test_boolean_list():
    a_list = [False, True, True]
    arr = Array(a_list)
    assert arr.dtype == 'b'

def test_int_list():
    a_list = [7, -1, 9]
    arr = Array(a_list)
    assert arr.dtype == 'q'

def test_float_list():
    a_list = [1, 2.3, 3]
    b_list = [2.4, 1, 9]
    c_list = [1, 3, 4.5]
    arr = Array(a_list)
    arr1 = Array(b_list)
    arr2 = Array(c_list)
    assert arr.dtype == 'd'
    assert arr1.dtype == 'd'
    assert arr2.dtype == 'd'