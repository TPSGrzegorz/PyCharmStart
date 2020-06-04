def split_and_join(line):
    # write your code here
    newString = "-".join(line.split())
    print(newString)


if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)
