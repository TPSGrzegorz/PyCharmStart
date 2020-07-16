import re

PATTERN = r'[QWRTYPSDFGHJKLZXCVBNMqwrtypsdfghjklzxcvbnm]?([AEIOUaeiou]{2,})[QWRTYPSDFGHJKLZXCVBNMqwrtypsdfghjklzxcvbnm]'
lista = re.findall(PATTERN,'abaabaabaabaae')
if lista != []:
    print('\n'.join(lista))
else:
    print('-1')