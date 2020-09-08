cube = lambda x: x**3 # complete the lambda function

def fibonacci(n):
    result = list()
    a = 0
    b = 1
    if n == 0:
        return result
    if n == 1:
        result.append(a)
        return result
    elif n == 2:
        result.append(a)
        result.append(b)
        return result
    else:
        result.append(a)
        result.append(b)
        for i in range(2, n):
            result.append(result[-1] + result[-2])
        return result

if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))