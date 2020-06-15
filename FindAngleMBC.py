import math

AB = int(input())
BC = int(input())
result = round(math.degrees(math.atan2(AB, BC)))
print(f'{result}°')