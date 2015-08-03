import datetime

pacific = datetime.timezone(datetime.timedelta(hours=-8))
eastern = datetime.timezone(datetime.timedelta(hours=-5))

naive = datetime.datetime(2014, 4, 21, 9)

aware = datetime.datetime(2014, 4, 21, 8, tzinfo=pacific)

print(naive)
print(aware)
print(aware.astimezone(eastern))
