A = [1, 2, 3]
B = [6, 5, 4]
C = [7, 8, 9]
X = [A] + [B] + [C]

print(*zip(X))

n, x = map(int, input().split())
val = [list(map(float, input().split())) for _ in range(x)]
results = [sum(col)/len(col) for col in zip(*val)]

for result in results:
    print(f'{result:.1f}')



