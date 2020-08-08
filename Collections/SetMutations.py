len1 = int(input())
A = set(map(int, input().split()))
n = int(input())

for i in range(n):
    comand, *_ = list(input().split())
    B = set(map(int, input().split()))
    eval('A.' + comand + '(B)')
print(sum(A))