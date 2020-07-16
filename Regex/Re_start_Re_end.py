import re
value = input()
PATTERN = input()

len_value = len(value)
len_PATTERN = len(PATTERN)
pattern = re.compile(PATTERN)


if re.search(pattern , value):
    for i in range(len_value - len_PATTERN+1):
        x = i + len_PATTERN
        m = re.search(pattern , value[i:(i+len_PATTERN)])
        if m:
            result = (m.start()+i, m.end() -1 + i)
            print(result)
else:
    print((-1, -1))
