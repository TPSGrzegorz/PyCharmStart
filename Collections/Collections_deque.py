from collections import deque
n = int(input())
d = deque()
for i in range(n):
    to_uppack= list(input().split())
    if len(to_uppack) == 2:
        command, item = to_uppack
        arg = int(item)
        eval('d.' + command + '(arg)')
    else:
        command = to_uppack[0]
        eval('d.' + command + '()')
print(*d)