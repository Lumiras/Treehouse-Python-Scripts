import datetime

now = datetime.datetime.now()
hour = datetime.timedelta(hours=1)
workday = hour * 9
tomorrow = datetime.datetime.now().replace(hour=9, minute=0) + datetime.timedelta(days=1)

print(now.date())
print(now.time())
print(now - datetime.timedelta(days=5))
print(tomorrow)
print(tomorrow + workday)
