import re


def is_valid_float(number: str) -> bool:
    """
    >>> is_valid_float('-1.0234')
    True
    >>> is_valid_float('-4')
    False
    >>> is_valid_float('432')
    False
    >>> is_valid_float('.432')
    True
    >>> is_valid_float('..432')
    False
    >>> is_valid_float('+.432')
    True
    >>> is_valid_float('-+.432')
    False

    :param number:
    :return:
    """
    PATTERN = r'^([-+]{0,1})(((([0-9]{1})|([1-9][0-9]){1,})(\.))|(\.))([0-9]{1,})$'
    PATTERN2 = r'^([-+]?)((((\d)|([1-9]\d*))(\.))|(\.))(\d+)$'
    PATTERN3 = r'^[-+]?(((\d|([1-9]\d*))\.)|(\.))(\d+)$'
    if re.match(PATTERN3, number):
        return True
    else:
        return False


# n = int(input())
#
# for _ in range(n):
#     print(is_valid_float(input()))
