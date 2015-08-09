import datetime

now = datetime.datetime.now()
birthday = datetime.datetime.strptime('2015-11-01', '%Y-%m-%d')
birthday_party = datetime.datetime.strptime('2015-11-03 14:00', '%Y-%m-%d %H:%M')

print(now.strftime('%A, %B %d, %Y'))
print(now.strftime('%m/%d/%y'))
print(now.strftime('%D'))

print(birthday)
print(birthday_party)
