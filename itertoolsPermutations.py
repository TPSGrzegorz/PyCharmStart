from itertools import permutations

string, n = input().split()
result = list(permutations(sorted(string), int(n)))
for i in result:
    print(''.join(i))

#print(*[''.join(i) for i in permutations(sorted(string), int(n))], sep='\n')
