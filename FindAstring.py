def count_substring(string, sub_string):
    howMany = 0
    index = 0
    while string.count(sub_string, index, len(string)) != 0:
        howMany += 1
        index = string.index(sub_string, index) + 1
    return howMany


if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()

    count = count_substring(string, sub_string)
    print(count)