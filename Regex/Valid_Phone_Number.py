import re


def is_valid_email(phoneNumber: str) -> str:
    PATTERN = r'^[987][0-9]{9}$'

    if re.match(PATTERN, phoneNumber):
        return 'YES'
    else:
        return 'NO'


n = int(input())
for i in range(n):
    print(is_valid_email(input().strip()))
