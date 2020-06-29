# Function Arguments Numbers to Human
# sorce: https://python.astrotech.io/basics/function/arguments.html#function-arguments-numbers-to-human

from typing import Dict


def numbers_to_human(number: float):
    """
    >>> numbers_to_human(1969)
    'one thousand nine hundred sixty nine'

    >>> numbers_to_human(31337)
    'thirty one thousand three hundred thirty seven'

    >>> numbers_to_human(13.37)
    'thirteen and thirty seven hundredths'

    >>> numbers_to_human(31.337)
    'thirty one three hundreds thirty seven thousands'

    >>> numbers_to_human(-1969)
    'minus one thousand nine hundred sixty nine'

    >>> numbers_to_human(-31.337)
    'minus thirty one thousands and three hundreds thirty seven'

    >>> numbers_to_human(-49.35)
    'minus forty nine and thirty five hundreds'

    """

    ALPHABET = {
        '0': 'zero',
        '1': 'one',
        '2': 'two',
        '3': 'three',
        '4': 'four',
        '5': 'fife',
        '6': 'six',
        '7': 'seven',
        '8': 'ait',
        '9': 'nine',
        '-': 'minus',
        '.': 'and',
        '10': 'ten',
        '11': 'eleven',
        '12': 'twelve',
        '13': 'thirteen',
        '14': 'fourteen',
        '15': 'fifteen',
        '16': 'sixteen',
        '17': 'seventeen',
        '18': 'eighteen',
        '19': 'nineteen',
        '2X': 'twenty',
        '3X': 'thirty',
        '4X': 'forty',
        '5X': 'fifty',
        '6X': 'sixty',
        '7X': 'seventy',
        '8X': 'eighty',
        '9X': 'ninety',
        '1XX': 'hundred',
        '1XXX': 'thousand'
    }
    result = []
    if number < 0:
        result.append('minus')
        number *= -1
    number_in_string = str(number)
    number_len = len(number_in_string)
    dotTrue = True if '.' in number_in_string else False

    if dotTrue:
        pass
    else:
        if number_len == 5:
            if 9999 < number <= 99999:
                if 9999 < number <= 19999:
                    result.append(ALPHABET.get(number_in_string[0:2]))
                    result.append(ALPHABET.get('1XXX'))
                else:
                    result.append(ALPHABET.get((number_in_string[0] + 'X')))
                    result.append(ALPHABET.get(number_in_string[1]))
                    result.append(ALPHABET.get('1XXX'))

                result.append(ALPHABET.get(number_in_string[2]))
                result.append(ALPHABET.get('1XX'))
                if 9 < number % 100 <= 19:
                    result.append(ALPHABET.get(number_in_string[3:5]))
                elif 0 <= number % 100 <= 9:
                    result.append(ALPHABET.get(number_in_string[4]))
                else:
                    result.append(ALPHABET.get((number_in_string[3]+'X')))
                    result.append(ALPHABET.get(number_in_string[4]))
        if number_len == 4:
            if 999 < number <= 9999:
                result.append(ALPHABET.get(number_in_string[0]))
                result.append(ALPHABET.get('1XXX'))

                result.append(ALPHABET.get(number_in_string[1]))
                result.append(ALPHABET.get('1XX'))
                if 9 < number % 100 <= 19:
                    result.append(ALPHABET.get(number_in_string[2:4]))
                elif 0 <= number % 100 <= 9:
                    result.append(ALPHABET.get(number_in_string[3]))
                else:
                    result.append(ALPHABET.get((number_in_string[2]+'X')))
                    result.append(ALPHABET.get(number_in_string[3]))

    return ' '.join(result)


print(numbers_to_human(1969))
print(numbers_to_human(31337))
print(numbers_to_human(-1969))
