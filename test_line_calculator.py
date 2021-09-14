# test_line_calculator.py
# Author: Alex Thomason

import pytest       # Import Pytest to use the decorator

# @pytest is a decorator - must be put before the test function. A decorator performs the function before and after the function runs.
@pytest.mark.parametrize("point1_tuple,point2_tuple,x_point_value,expected",[   
((0,2),(2,6), 2, 4),
((0,2),(2,6), 3, 8),
((0,1),(2,7), 1, 4)])

def test_line_calculator(point1_tuple,point2_tuple,x_point_value,expected):
    from line_calculator import line_calculator
    answer = line_calculator(x_point_value)
    assert answer == expected
