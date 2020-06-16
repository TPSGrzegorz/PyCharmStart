def kalkulator():
    print("""Witam Cię w programie Kalkulator.
Dostępne operacje to +,-,*,/,//,%,**.
Format wprowadzania danych to <wartosc1> <operacja> <wartosc2>.
Przykład: 2 + 2'""")
    while True:
        a, operacja, b = input("Podaj równanie do policznie: ").split()
        a = int(a)
        b = int(b)
        wynik = eval(f'{a}{operacja}{b}')
        print(f'Wynik operacji {a} {operacja} {b} to: {wynik}')
        decyzja = input("Czy chcesz wykonać kolejne działanie t lub n: ")
        if decyzja == "n" or decyzja is None:
            break


def main():
    kalkulator()


if __name__ == "__main__":
    main()
