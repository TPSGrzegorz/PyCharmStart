# from collections import OrderedDict
#
# ordinary_dictionary = {}
# ordinary_dictionary['a'] = 1
# ordinary_dictionary['b'] = 2
# ordinary_dictionary['c'] = 3
# ordinary_dictionary['d'] = 4
# ordinary_dictionary['e'] = 5
#
# print(ordinary_dictionary)
#
#
# ordered_dictionary = OrderedDict()
# ordered_dictionary['a'] = 1
# ordered_dictionary['b'] = 2
# ordered_dictionary['c'] = 3
# ordered_dictionary['d'] = 4
# ordered_dictionary['e'] = 5
#
# print(ordered_dictionary)
from collections import OrderedDict

n = int(input())
ordered_dictionary = OrderedDict()
for _ in range(n):
    *product, price = input().split()
    label = ' '.join(product)
    if label in ordered_dictionary:
        ordered_dictionary[label] += int(price)
    else:
        ordered_dictionary[label] = int(price)

print(*[" ".join([label, str(price)]) for label, price in ordered_dictionary.items()], sep="\n")

