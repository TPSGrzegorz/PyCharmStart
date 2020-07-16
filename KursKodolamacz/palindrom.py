def is_palindrom(word: str) -> bool:
    # """
    # :param word:
    # :return:
    #
    # >>> is_palindrom('aaaaaaaaaaaajaaaaaaaaaaaa')
    # True
    # >>> is_palindrom('bbbabbbb')
    # False
    # """
    n = len(word)
    j = n
    for i in range(n // 2):
        if word[i] != word[n - i - 1]:
            return False
    return True


def is_palindrom2(word: str) -> bool:
    # """
    # :param word:
    # :return:
    #
    # >>> is_palindrom2('aaaaaaaaaaaajaaaaaaaaaaaa')
    # True
    # >>> is_palindrom2('bbbabbbb')
    # False
    # """
    return word == word[::-1]


def test():
    """Stupid test function"""
    L = [i for i in range(100)]
def main():
    pass

if __name__ == '__main__':
    import timeit
    print(timeit.timeit("test()", setup="from __main__ import test"))
    print('safafa')
