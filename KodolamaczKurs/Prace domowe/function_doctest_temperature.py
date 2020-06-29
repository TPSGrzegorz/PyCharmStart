# Function Doctest Temperature
# sorce: https://python.astrotech.io/basics/function/doctest.html#function-doctest-temperature

def celsius_to_kelvin(degrees):
    """
    >>> celsius_to_kelvin(0)
    273.15
    >>> celsius_to_kelvin(1)
    274.15
    >>> celsius_to_kelvin(-1)
    272.15
    >>> celsius_to_kelvin('a')
    Traceback (most recent call last):
        ...
    TypeError: Invalid argument
    >>> celsius_to_kelvin([0, 1])
    [273.15, 274.15]
    >>> celsius_to_kelvin((0, 1))
    (273.15, 274.15)
    >>> celsius_to_kelvin({0, 1})
    {273.15, 274.15}

    """

    datatype = type(degrees)

    if type(degrees) in {list, tuple, set, frozenset}:
        return datatype(celsius_to_kelvin(x) for x in degrees)

    if datatype not in {int, float}:
        raise TypeError('Invalid argument')

    kelvin = degrees + 273.15

    if kelvin < 0.0:
        raise ValueError('Negative Kelvin')

    return float(kelvin)