n, N = int(input()), list(input().split())
print(all([int(x) >= 0 for x in N]) and any([y == y[::-1] for y in N]))