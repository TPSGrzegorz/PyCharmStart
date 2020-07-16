from datetime import datetime
from pytz import timezone

# Kosmodrom Bajkonur, Kazachstan
# Cape Canaveral, FL, USA
# Houston, TX, USA

# South Pole
# North Pole

# Tokyo, Japan
# Sydney, Australia
# Auckland, Nowa Zelandia

ZONES = [
    'UTC',
    'Europe/Warsaw',
    'Asia/Almaty',
    'Europe/Moscow',
    'America/New_York',
    'Europe/London',
    'Antarctica/McMurdo',
    'Asia/Tokyo',
    'Australia/ACT',
    'Pacific/Auckland'
]

UTC = timezone('UTC')
WAW = timezone('Europe/Warsaw')
BAIKONUR = timezone('Asia/Almaty')
MOSCOW = timezone('Europe/Moscow')

DATA = '1969-07-21 02:56:15 UTC'
format = '%Y-%m-%d %H:%M:%S %Z'
A = datetime.strptime(DATA, format)
A = UTC.localize(A)

AA = A.astimezone(WAW)
AMOSCOW = A.astimezone(MOSCOW)

print(AA)
print(AMOSCOW)