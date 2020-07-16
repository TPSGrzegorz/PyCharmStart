n = int(input())
for i in range(n):
    k = int(input())
    A = set(map(int, input().split()))
    m = int(input())
    B = set(map(int, input().split()))
    result = B.issubset(A)
    print(result)