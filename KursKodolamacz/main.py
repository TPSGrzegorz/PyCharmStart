
def main():
    krotka = [2, 3, 4, 5]
    krotka[1:2] = [33, 44, 55]
    krotka[7:8:] = [100]
    krotka = krotka.__add__([2222])
    print(krotka)

if __name__ == "__main__":
    main()
