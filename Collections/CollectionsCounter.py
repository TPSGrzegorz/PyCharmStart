def colection_cunter():
    from collections import Counter
    X = int(input())
    N = list(map(int, input().split()))
    x = int(input())
    result = 0
    dict_of_product = Counter(N)
    for i in range(x):
        size, cost = list(map(int, input().split()))
        if dict_of_product.get(size, 0) != 0:
            dict_of_product[size] -= 1
            result += cost

    print(result)


def main():
    colection_cunter()


if __name__ == "__main__":
    main()
