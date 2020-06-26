from itertools import combinations
from collections import Counter

def combination_function():
    s, k = input().split()
    #for i in range(1, int(k) + 1):
    #    for j in combinations(sorted(s), i):
    #        print(''.join(j))

    print(*[''.join(j) for i in range(1, int(k) + 1) for j in combinations(sorted(s), i)],sep='\n')

    # print(*((10 ** i // 9) * i for i in range(1, int(input()))), sep='\n')

def main():
    myList = [1, 1, 2, 3, 4, 5, 3, 2, 3, 4, 2, 1, 2, 3]
    c = Counter(myList)
    print(c)


if __name__ == "__main__":
    main()


def test_fc(a, b):
    """
    >>> test_fc(4 , 5)
    9
    >>> test_fc(1.0 , 1.0)
    2.0
    >>> test_fc('a' , 'b')
    'ab'
    :param a:
    :param b:
    :return: a + b
    """
    return a + b
