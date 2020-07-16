def mul_recur(a: int, n:int) -> int:
    """
    :param a:
    :param n:
    :return:

    >>> mul_recur(2,2)
    4
    >>> mul_recur(1,0)
    1
    >>> mul_recur(10,2)
    100
    """
    if n == 0:
        return 1
    if n == 1:
        return a
    half_pow =n//2
    half = mul_recur(a, half_pow)
    result =  half*half
    if n % 2 == 0:
        return result
    else:
        return  result * a



def main():
    result = mul_recur(2,256)
    print(result)




if __name__ == '__main__':
    main()