from itertools import combinations_with_replacement

def combination_function():
    s, k = input().split()
    print(*[''.join(j) for i in range(int(k), int(k) + 1) for j in combinations_with_replacement(sorted(s), i)],sep='\n')

combination_function()