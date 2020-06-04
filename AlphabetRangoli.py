import string
def rangoli(n):
    # your code goes here
    a = 97
    end = 'a'
    c = chr(a + n - 1)
    bb = 0
    for i in range(2 * n - 1):
        print(((c + '-') * i).rjust(2 * (n - 1), '-') + chr(a + abs(n - i - 1)) + (
                    ('-' + c) * i).ljust(2 * (n - 1), '-'))

    # print(chr(a+1).center(n, '-'))
    # for i in range(n//2 , 0, -1):
    # print((c * (i-1)).rjust(n//2 - 1, '-') + c + (c * (i-1)).ljust(n//2 - 1, '-'))


if __name__ == '__main__':
    size = list(map(int, input().split()))
    #rangoli(size[0])
    alpha = string.ascii_lowercase
    n = size[0]
    s = ''
    L = []
    for i in range(n):
        s = "-".join(alpha[i:n])
        L.append(s[::-1] + s[1:])
    width = len(L[0])

    for i in range(n - 1, 0, -1):
        print(L[i].center(width, "-"))

    for i in range(n):
        print(L[i].center(width, "-"))