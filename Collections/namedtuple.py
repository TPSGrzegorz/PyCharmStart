# # Example of use 1
# from collections import namedtuple
#
# Point = namedtuple('Point', 'x,y')
# pt1 = Point(1, 2)
# pt2 = Point(3, 4)
# dot_product = (pt1.x * pt2.x) + (pt1.y * pt2.y)
# print(dot_product)
#
#
# # Example of use 2
# Car = namedtuple('Car', 'Price Mileage Colour Class')
# xyz = Car(Mileage=30, Price=100000,  Colour='Cyan', Class='Y')
# print(xyz)
# print(xyz.Class)
#
# from collections import namedtuple
# n = int(input())
# Table = namedtuple('Table', 'ID MARKS NAME CLASS')
# lables = list(map(str,input().split()))
# indeks = lables.index('MARKS')
# print(indeks)
# print(lables)
# for record in range(n):
#     pass
#
# # for record in range(n):
# #     pass
#
# #print(f'{result/n:.2f}')


from collections import namedtuple
N = int(input())
label = input().strip().split()

Student = namedtuple('student',label)
my_sum = 0.0
for _ in range(N):
    my_sum += float(Student(*input().strip().split()).MARKS)
result = my_sum/N
print(f'{result:.2f}')
#print(sum(float(Student(*input().strip().split()).MARKS) for _ in range(N))/N)