n = int(input())
s = set(map(int, input().split()))
k = int(input())
for i in range(k):
    comand = list(input().split())
    if 'pop' == comand[0]:
        s.pop()
        continue
    if 'remove' == comand[0]:
        try:
            s.remove(int(comand[1]))
        except:
            continue
    if 'discard' == comand[0]:
        s.discard(int(comand[1]))
        continue
print(sum(s))