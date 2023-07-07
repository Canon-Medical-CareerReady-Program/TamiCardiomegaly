from math import sqrt

def distance(x1 : float, y1 : float, x2 : float, y2 : float) -> float:
    """ Calculate euclidean distance between two points """
    xdiff = x1 - x2
    ydiff = y1 - y2
    xdiff2 = xdiff * xdiff
    ydiff2 = ydiff * ydiff
    length = sqrt(xdiff2 + ydiff2)
    return length


def calculate_ratio(heart_length: float, thorax_length: float) -> float:
    """ Calculate ratio between heart and thorax """
    ratio = heart_length / thorax_length
    return ratio