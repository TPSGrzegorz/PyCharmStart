def merge_the_tools(string, k):
    # your code goes here
    temp_string: list = []
    list_string = list(string)
    subsegments_count: int = int(len(string)/k)
    for i in range(subsegments_count):
        temp_string = list_string[k * i : k * i + k]
        temp = list(range(k))
        temp_dict = dict(zip(temp_string, temp))
        string_to_print = ''.join(temp_dict.keys())
        print(string_to_print)

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)