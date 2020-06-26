from itertools import groupby

def compress_string():
    new = input()
    groups = []
    uniquekeys = []
    data = new
    for k, g in groupby(data):
        gg = len(list(g))
        groups.append(int(k))
        uniquekeys.append(gg)
    result = tuple(zip(uniquekeys,groups,))
    print(*result)


def main():
    compress_string()


if __name__ == "__main__":
    main()