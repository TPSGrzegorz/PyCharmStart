from datetime import datetime

print('ZADANIE 1')
DATA = '1969-07-21T02:56:15.123Z'
format = '%Y-%m-%dT%H:%M:%S.%fZ'
date = datetime.strptime(DATA, format)
print(DATA, '\n')

print('ZADANIE 2')
DATA = 'April 12, 1961 6:07 local time'

format = '%B %d, %Y %H:%M local time'
date = datetime.strptime(DATA, format)
print(date)
final_format = '%Y-%m-%dT%H:%M:%S.%fZ'
result = date.strftime(final_format)
print(result, '\n')

print('ZADANIE 3')
DATA = '"July 21st, 1969 2:56:15 AM UTC"'

format = '"%B %dst, %Y %I:%M:%S %p %Z"'

date2 = datetime.strptime(DATA, format)
final_format = '%Y/%d/%m %#I:%M %p'
result = date2.strftime(final_format)
print(result, '\n')

# ZADANIE 4
print('ZADANIE 4')

from typing import List
from pprint import pprint


LOGS = [
    "1969-07-14, 21:00:00, INFO, Terminal countdown started",
    "1969-07-16, 13:31:53, WARNING, S-IC engine ignition (#5)",
    "1969-07-16, 13:33:23, DEBUG, Maximum dynamic pressure (735.17 lb/ft^2)",
    "1969-07-16, 13:34:44, WARNING, S-II ignition",
    "1969-07-16, 13:35:17, DEBUG, Launch escape tower jettisoned",
    "1969-07-16, 13:39:40, DEBUG, S-II center engine cutoff",
    "1969-07-16, 16:22:13, INFO, Translunar injection",
    "1969-07-16, 16:56:03, INFO, CSM docked with LM/S-IVB",
    "1969-07-16, 17:21:50, INFO, Lunar orbit insertion ignition",
    "1969-07-16, 21:43:36, INFO, Lunar orbit circularization ignition",
    "1969-07-20, 17:44:00, INFO, CSM/LM undocked",
    "1969-07-20, 20:05:05, WARNING, LM powered descent engine ignition",
    "1969-07-20, 20:10:22, ERROR, LM 1202 alarm",
    "1969-07-20, 20:14:18, ERROR, LM 1201 alarm",
    "1969-07-20, 20:17:39, WARNING, LM lunar landing",
    "1969-07-21, 02:39:33, DEBUG, EVA started (hatch open)",
    "1969-07-21, 02:56:15, WARNING, 1st step taken lunar surface (CDR)",
    "1969-07-21, 02:56:15, WARNING, That's one small step for [a] man... one giant leap for mankind",
    "1969-07-21, 03:05:58, DEBUG, Contingency sample collection started (CDR)",
    "1969-07-21, 03:15:16, INFO, LMP on lunar surface",
    "1969-07-21, 05:11:13, DEBUG, EVA ended (hatch closed)",
    "1969-07-21, 17:54:00, WARNING, LM lunar liftoff ignition (LM APS)",
    "1969-07-21, 21:35:00, INFO, CSM/LM docked",
    "1969-07-22, 04:55:42, WARNING, Transearth injection ignition (SPS)",
    "1969-07-24, 16:21:12, INFO, CM/SM separation",
    "1969-07-24, 16:35:05, WARNING, Entry",
    "1969-07-24, 16:50:35, WARNING, Splashdown (went to apex-down)",
    "1969-07-24, 17:29, INFO, Crew egress",
]
my_list = []
for log in LOGS:
    date, time, level, message = log.split(maxsplit=3)
    date = f'{date} {time}'


    if len(time) == 6:
        format = '%Y-%m-%d, %H:%M,'
    else:
        format = '%Y-%m-%d, %H:%M:%S,'
    date = datetime.strptime(date, format)

    my_dict = {
        'date': date,
        'level' : level,
        'message': message
    }
    my_list.append(my_dict)
pprint(my_list)

# result: List[dict] = [
#
#      {'date': datetime.datetime(1969, 7, 14, 21, 0),
#       'level': 'INFO',
#       'message': 'Terminal countdown started'},
#
#      {'date': datetime.datetime(1969, 7, 16, 13, 31, 53),
#       'level': 'WARNING',
#       'message': 'S-IC engine ignition (#5)'},
#
#      {'date': datetime.datetime(1969, 7, 16, 13, 33, 23),
#       'level': 'DEBUG',
#       'message': 'Maximum dynamic pressure (735.17 lb/ft^2)'},
#
# ...]