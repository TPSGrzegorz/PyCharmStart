if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    temp = max(arr)
    while max(arr) == temp:
        arr.remove(temp)

    print(max(arr))