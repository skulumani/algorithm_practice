import numpy as np
from binary_search import bin_search

def test_binary_search_first():
    n = 5
    arr = [1, 2, 3, 4, 5]
    x = 4
    true_key = 3
    key = bin_search(arr, 0 , 0, x)
    np.testing.assert_equal(key, true_key)

def test_binary_search_second():
    n = 5
    arr = [11, 22, 33, 44, 55]
    x = 445
    true_key = -1
    key = bin_search(arr, 0, 0, x)
    np.testing.assert_equal(key, true_key)

def test_binary_search_even_array():
    n = 8
    arr = [1, 2, 3, 4, 5, 6, 7, 8]
    x = 7
    true_key = 6
    key = bin_search(arr, 0, 0, x)
    np.testing.assert_equal(key, true_key)

def test_binary_search_end_item():
    n = 68
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 15, 17, 18, 19, 20, 21, 22, 25, 26, 27, 29, 31, 32, 33, 35, 36, 40, 41, 42, 43, 46, 47, 48, 51, 54, 55, 56, 57, 58, 61, 63, 64, 65, 67, 69, 71, 74, 77, 78, 79, 80, 81, 82, 83, 85, 86, 87, 88, 89, 90, 91, 93, 95, 99, 100]
    x = 100
    true_key = 67
    key = bin_search(arr, 0, 0, x)
    np.testing.assert_equal(key, true_key)
