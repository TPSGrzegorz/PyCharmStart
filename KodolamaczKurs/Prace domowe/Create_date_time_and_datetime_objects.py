from datetime import datetime, date, time

my_birthday = date(1987, 9, 25)
my_time = time(5, 24, 5)
now = datetime.now()

print(my_birthday)
print(my_time)
print(now)

print('######## Zadanie 2 ########')
dt = datetime.now()
print(dt)
d = dt.date()
print(d)
t = dt.time()
print(t)