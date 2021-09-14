# line_calculator.py
# Author: Alex Thomason

def line_calculator(point1_tuple,point2_tuple,x_point_value):
    slope = (point2_tuple[1]-point1_tuple[1]) / (point2_tuple[0]-point1_tuple[0]) 
    y_intercept = point2_tuple[1] - slope * point2_tuple[0]
    y_point_value = slope* x_point_value + y_intercept
    return y_point_value

def slope_calculator(point1_tuple,point2_tuple):
    slope = (point2_tuple[1]-point1_tuple[1]) / (point2_tuple[0]-point1_tuple[0])
    return slope

if __name__ == "__main__":
    y_point = line_calculator((0,2),(2,6), 2)

