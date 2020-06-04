def ex1():
    x = int(input("Podaj liczbę = "))
    print(x ** 2)


def ex2():
    str = input("Podaj tekst do wyświetlenie = ")
    return print(str)


def ex3(value1, value2, value3="Jestem domyślny", value4="Ja tez", value5=25):
    print(str(value1) + " " + value2)
    print(value3 + " " + value4 + " " + str(value5))


def ex5(x, y = 4):
    """ Konwertuję wartość x na wartośc typu float
    :param x: int,
    :param y: int,
    :return: float x"""
    try:
        temp = float(x)
        print(temp)
    except ValueError:
        print("Zła wartośc")


if __name__ == '__main__':
    ex5(230)
    ex5(424)
    ex3(value1=2, value2="To jest tekst")
    ex1()
    ex2()
