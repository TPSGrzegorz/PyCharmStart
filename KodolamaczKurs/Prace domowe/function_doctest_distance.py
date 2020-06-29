# Function Doctest Distance
# https://python.astrotech.io/basics/function/doctest.html#function-doctest-distance


def kilometers_to_meters(kilometers):
    """
    >>> kilometers_to_meters(-1)
    Traceback (most recent call last):
        ...
    ValueError: Argument must be positive number

    >>> kilometers_to_meters(1)
    1000.0
    >>> kilometers_to_meters(0)
    0.0
    >>> kilometers_to_meters(12.3)
    12300.0
    >>> kilometers_to_meters(12)
    12000.0
    >>> kilometers_to_meters('12')
    Traceback (most recent call last):
    ...
    TypeError: Invalid argument

    >>> kilometers_to_meters([12])
    Traceback (most recent call last):
    ...
    TypeError: Invalid argument

    :param kilometers:
    :return: value in meters
    """
    datatype = type(kilometers)
    if datatype not in {int, float}:
        raise TypeError('Invalid argument')
    if kilometers < 0.0:
        raise ValueError('Argument must be positive number')
    return kilometers * 1000.0
