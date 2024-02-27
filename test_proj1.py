import pytest, tracemalloc

from proj1 import matrix_multiply

import numpy as np
# when tracing memory, using command: pytest -s test_proj1.py to show memory usage details
def setup_function(function):
   
    tracemalloc.start()

def teardown_function(function):
    
    snapshot = tracemalloc.take_snapshot()
    top_stats = snapshot.statistics('lineno')

    print(f"[ Top 10 memory allocations for {function.__name__} ]")
    for stat in top_stats[:10]:
        print(stat)
    
    tracemalloc.stop()
    
def test_large_matrices():

    A = np.random.rand(100, 100)
    B = np.random.rand(100, 100)
    expected_result = np.dot(A, B)
    assert np.allclose(matrix_multiply(A.tolist(), B.tolist()), expected_result)

def test_non_square_matrices():
    A = np.random.rand(2, 3)
    B = np.random.rand(3, 4)
    expected_result = np.dot(A, B)
    assert np.allclose(matrix_multiply(A.tolist(), B.tolist()), expected_result)

def test_floating_point_numbers():
    A = [[1.5, 2.5], [3.5, 4.5]]
    B = [[2.5, 0.5], [1.5, 2.5]]
    expected_result = np.dot(A, B)
    assert np.allclose(matrix_multiply(A, B), expected_result)


def test_input():
    A = [[1, 2], [3, 4]]
    B = [[2, 0], [1, 2]]
    assert matrix_multiply(A, B) == [[4, 4], [10, 8]]

def test_identity():
    I = [[1, 0], [0, 1]]
    A = [[1, 2], [3, 4]]
    assert matrix_multiply(A, I) == A

def test_cols_rows():
    A = [[1, 2, 3], [4, 5, 6]]
    B = [[7, 8], [9, 10]]
    with pytest.raises(ValueError):
        matrix_multiply(A, B)

def test_empty():
    A = []
    B = [[1, 2], [3, 4]]
    with pytest.raises(ValueError):
        matrix_multiply(A, B)

def test_scalar():
    A = [[3]]
    B = [[4]]
    assert matrix_multiply(A, B) == [[12]]
