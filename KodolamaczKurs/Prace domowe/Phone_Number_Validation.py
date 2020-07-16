import re

def phone_number_valid(number: str) -> bool:
    """
    >>> phone_number_valid('+48 (12) 355 5678')
    False
    >>> phone_number_valid('+48 123 555 678')
    True
    >>> phone_number_valid('123 555 678')
    False
    >>> phone_number_valid('+48 12 355 5678')
    True
    >>> phone_number_valid('+48 123-555-678')
    False
    >>> phone_number_valid('+48 123 555 6789')
    True
    >>> phone_number_valid('+1 (123) 555-6789')
    False
    >>> phone_number_valid('+1 (123).555.6789')
    False
    >>> phone_number_valid('+1 800-python')
    False
    >>> phone_number_valid('+48123555678')
    False
    >>> phone_number_valid('+48 123 555 678 wew. 1337')
    True
    >>> phone_number_valid('+48 123555678,1')
    False
    >>> phone_number_valid('+48 123555678,1,2,3')
    False

    :param number:
    :return:
    """

    PATTERN = r'^\+[0-9]{2}\s[0-9]{2,3}\s[0-9]{3}\s[0-9]{3,4}.*$'

    if re.match(PATTERN, number):
        return True
    else:
        return False

# def is_valid_email(email: str) -> bool:
#     """Function check email address against Regular Expression
#     >>> is_valid_email('jose.jimenez@nasa.gov')
#     True
#     >>> is_valid_email('José.Jiménez@nasa.gov')
#     True
#     >>> is_valid_email('+jose.jimenez@nasa.gov')
#     False
#     >>> is_valid_email('jose.jimenez+@nasa.gov')
#     True
#     >>> is_valid_email('jose.jimenez+newsletter@nasa.gov')
#     True
#     >>> is_valid_email('jose.jimenez@.gov')
#     False
#     >>> is_valid_email('@nasa.gov')
#     False
#     >>> is_valid_email('jose.jimenez@nasa.g')
#     False
#     """
#     PATTERN = r'^[a-zA-Z0-9][\w.+-]*@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]{2,20}$'
#
#     if re.match(PATTERN, email):
#         return True
#     else:
#         return False
DATA = [
    '+48 (12) 355 5678',
    '+48 123 555 678',
    '123 555 678',
    '+48 12 355 5678',
    '+48 123-555-678',
    '+48 123 555 6789',
    '+1 (123) 555-6789',
    '+1 (123).555.6789',
    '+1 800-python',
    '+48123555678',
    '+48 123 555 678 wew. 1337',
    '+48 123555678,1',
    '+48 123555678,1,2,3',
]

for number in DATA:
    result = phone_number_valid(number)
    print(f'{result}\t{number}')

## Alternative solution
import re


PATTERN = r'^'                      # Start String
PATTERN += r'\+\d{2} ('             # Country Code
PATTERN += r'(\d{2} \d{3} \d{4})'   # Work Phone
PATTERN += r'|'                     # Or
PATTERN += r'(\d{3} \d{3} \d{3})'   # Mobile
PATTERN += r')$'

MOBILE = r'(\+\d\d \d\d\d \d\d\d \d\d\d)'
WORK = r'(\+\d\d \d\d \d\d\d \d\d\d\d)'
PATTERN = f'^{MOBILE}|{WORK}$'