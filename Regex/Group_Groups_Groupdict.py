import re
m = re.match(r'.*?([A-Za-z0-9])\1+.*', input().strip())
print(m.group(0))
print(m.group(1) if m else -1)
