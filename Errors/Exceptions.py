
n = int(input())

for _ in range(n):
    try:
        a, b = list(map(int, input().split()))
        result = a//b
    except Exception as e:
        print(f'Error Code:{e}')
