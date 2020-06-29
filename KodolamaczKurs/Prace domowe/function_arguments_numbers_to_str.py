# Function Arguments Numbers to Str
# sorce: https://python.astrotech.io/basics/function/arguments.html#function-arguments-numbers-to-str

from typing import Dict


def pilot_say(number: float):
    """
    >>> pilot_say(1969)
    'one niner six niner'

    >>> pilot_say(31337)
    'tree one tree tree seven'

    >>> pilot_say(13.37)
    'one tree and tree seven'

    >>> pilot_say(31.337)
    'tree one and tree tree seven'

    >>> pilot_say(-1969)
    'minus one niner six niner'

    >>> pilot_say(-31.337)
    'minus tree one and tree tree seven'

    >>> pilot_say(-49.35)
    'minus fower niner and tree fife'

    """

    NUMBER = {
        0: 'zero',
        1: 'one',
        2: 'two',
        3: 'tree',
        4: 'fower',
        5: 'fife',
        6: 'six',
        7: 'seven',
        8: 'ait',
        9: 'niner',
    }
    ALPHABET: Dict[str, str] = {str(k): v for k, v in NUMBER.items()}
    ALPHABET['-'] = 'minus'
    ALPHABET['.'] = 'and'

    result = [ALPHABET.get(c) for c in str(number)]

    return ' '.join(result)
