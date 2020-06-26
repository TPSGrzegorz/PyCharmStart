from itertools import product
from pprint import pprint

K, M = map(int, input().split())
big_list = []
result = 0
for i in range(K):
    n, *my_list = map(int, input().split())
    my_list = list(my_list)
    my_list = list(map(lambda x: (x**2) % M, my_list))
    big_list.append(my_list)
print(max(list(map(lambda x: (sum(x)) % M, product(*big_list)))))

#pprint(list(product(big_list)))