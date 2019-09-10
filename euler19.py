import datetime

count = 0

for year in range(1901,2001,1):

    for month in range(1,13,1):

        weekday = datetime.date(year, month, 01).weekday()

        if weekday == 6:
            count += 1

print count