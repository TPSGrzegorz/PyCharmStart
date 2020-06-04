def doorMant(n, m):
    # your code goes here
    c = ".|."
    string = "WELCOME"
    for i in range(n//2):
        print((c * i).rjust(m//2 - 1, '-') + c + (c * i).ljust(m//2 - 1, '-'))
    print(string.center(m, '-'))
    for i in range(n//2 , 0, -1):
        print((c * (i-1)).rjust(m//2 - 1, '-') + c + (c * (i-1)).ljust(m//2 - 1, '-'))


if __name__ == '__main__':
    size = list(map(int, input().split()))
    doorMant(size[0], size[1])
