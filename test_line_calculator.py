# test_line_calculator.py
# Author: Alex Thomason

import pytest       # Import Pytest to use the decorator


# @pytest is a decorator - must be put before the test function.
# A decorator performs the function before & after the function runs
@pytest.mark.parametrize("point1_tuple, point2_tuple, x_point_value, expected", [
    ((0, 2), (2, 6), 2, 6),
    ((0, 2), (2, 6), 3, 8),
    ((0, 1), (2, 7), 1, 4)])
def test_line_calculator(point1_tuple, point2_tuple, x_point_value, expected):
    from line_calculator import line_calculator
    answer = line_calculator(point1_tuple, point2_tuple, x_point_value)
    assert answer == expected


@pytest.mark.parametrize("point1_tuple, point2_tuple, expected", [
    ((0, 2), (2, 6), 2),
    ((0, 1), (2, 7), 3)])
def test_slope_calculator(point1_tuple, point2_tuple, expected):
    from line_calculator import slope_calculator
    answer = slope_calculator(point1_tuple, point2_tuple)
    assert answer == expected


@pytest.mark.parametrize("point_tuple, slope,expected", [
    ((2, 6), 2, 2),
    ((2, 7), 3, 1)])
def test_y_intercept_calculator(point_tuple, slope, expected):
    from line_calculator import y_intercept_calculator
    answer = y_intercept_calculator(point_tuple, slope)
    assert answer == expected


@pytest.mark.parametrize("slope, y_intercept, x_point_value, expected", [
    (2, 2, 2, 6),
    (3, 1, 1, 4)])
def test_y_point_calculator(slope, y_intercept, x_point_value, expected):
    from line_calculator import y_point_calculator
    answer = y_point_calculator(slope, y_intercept, x_point_value)
    assert answer == expected
