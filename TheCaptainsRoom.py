k = int(input())
A = list(map(int, input().split()))
setA = set(A)
result = 0

print(((sum(setA)*k)-(sum(A)))//(k-1))

