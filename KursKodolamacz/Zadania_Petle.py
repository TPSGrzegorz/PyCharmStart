def main():
    print(*list(map(lambda x: x * 2, range(0, 51))), sep=',')
    print(*list(filter(lambda x: x % 2 != 0, range(0, 100))), sep=',')
    print(*[2 ** i for i in range(10) if 2 ** i <= 256], sep=',')

    liczba = 31
    is_prime(31)
    is_prime(2)
    is_prime(17)
    is_prime(4)
    is_prime(9)

def is_prime(number):
    is_prime_number = True
    if number % 2 == 0 and number > 2:
        is_prime_number = False
    else:
        for i in range(3, int(number ** 0.5)+1, 2):
            if number % i == 0:
                is_prime_number = False
                break
    print(f'Liczba {number} {"jest liczbą pierwszą" if is_prime_number else "nie jest liczba pierwsza"}')


if __name__ == "__main__":
    main()
