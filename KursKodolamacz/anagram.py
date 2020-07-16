def is_anagram_simple(word_1: str, word_2: str) -> bool:
    if len(word_1) != len(word_2):
        return False
    return sorted(word_1) == sorted(word_2)


def is_anagram_dict(word_1: str, word_2: str) -> bool:
    n = len(word_1)
    if n != len(word_2):
        return False
    dict_1 = {}
    dict_2 = {}
    for i in range(n):
        c = word_1[i]
        if word_1[i] in dict_1.keys():
            dict_1[c] += 1
        else:
            dict_1[c] = 1

        c = word_2[i]
        if c in dict_2.keys():
            dict_2[c] += 1
        else:
            dict_2[c] = 1

    return dict_1 == dict_2


# def is_anagram_dict_comp(word_1: str, word_2: str) -> bool:
#     if len(word_1) != len(word_2):
#         return False
#     dict_1 = {}
#     dict_2 = {}
#     sd = {dict_1[a] + 1 if a in dict_1.keys() else a:1 for a in word_1}
#     dict_2 = {k: 1 if k not in dict_2 else dict_2[k] + 1 for k in word_2}
#     print(dict_1)
#
#     print(sd)
#
#     return dict_1 == dict_2


print(is_anagram_dict('wooord', 'odrowo'))
print(is_anagram_dict('abbbcdefg', 'gbfabcbed'))
print(is_anagram_dict_comp('abbbcdefgbbb', 'gbfabcbedddd'))