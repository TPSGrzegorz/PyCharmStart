from datetime import datetime, timedelta

a = '1902-12-13 20:45:53 UTC'
b = '1970-01-01 00:00:00 UTC'
c = '2038-01-19 03:14:07 UTC'

format = '%Y-%m-%d %H:%M:%S %Z'
A = datetime.strptime(a, format)
A = datetime(year=A.year, month=A.month, day=A.day, hour=A.hour, minute=A.minute, second=A.second, microsecond=0, tzinfo=A.tzinfo)

B = datetime.strptime(b, format)
C = datetime.strptime(c, format)

#resultB = datetime.timestamp(B)
resultC = datetime.timestamp(C)
#print(resultB)
print(resultC)
