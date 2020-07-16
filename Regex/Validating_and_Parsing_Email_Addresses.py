import email.utils
import re
n = int(input())
PATTERN = r'^[A-Z]([A-Z0-9-._]+)@[A-Z]+\.[A-Z]{1,3}$'
for _ in range(n):
    result = email.utils.parseaddr(input())
    if re.match(PATTERN, result[1],flags=re.IGNORECASE):
        print(email.utils.formataddr(result))
