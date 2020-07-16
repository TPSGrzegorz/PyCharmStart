from datetime import datetime, timedelta, date


def duration(dt):
    years, seconds = divmod(dt.total_seconds(), YEAR)
    months, seconds = divmod(seconds, MONTH)
    days, seconds = divmod(seconds, DAY)
    hours, seconds = divmod(dt.seconds, HOUR)
    minutes, seconds = divmod(seconds, MINUTE)

    return {
        'years': int(years),
        'months': int(months),
        'days': int(days),
        'hours': int(hours),
        'minutes': int(minutes),
        'seconds': int(seconds),
    }


SECOND = 1
MINUTE = 60 * SECOND
HOUR = 60 * MINUTE
DAY = 24 * HOUR
MONTH = 30.436875 * DAY  # Average days a month in solar calendar
YEAR = 365.2425 * DAY  # Solar calendar


delta = int(8 * YEAR + 3*MONTH + 8 * DAY + 20 * HOUR + 49 * MINUTE + 15 * SECOND)

deltatime = timedelta( seconds= delta)

data = datetime.now()
result = data - deltatime
print(result)

my_birthday = datetime(1987, 9, 25, 5, 0, 0)

dt = result - my_birthday

result2 = duration(dt)

print(result2)

