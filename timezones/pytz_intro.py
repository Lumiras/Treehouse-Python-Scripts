import datetime
import pytz

pacific = pytz.timezone('US/Pacific')
eastern = pytz.timezone('US/Eastern')
auckland = pytz.timezone('Pacific/Auckland')
mumbai = pytz.timezone('Asia/Calcutta')

fmt = '%Y-%m-%d %H:%M:%S %Z%z'

utc = pytz.utc

apollo_13_naive = datetime.datetime(1970, 4, 11, 14, 13)
apollo_13_eastern = eastern.localize(apollo_13_naive)

start = pacific.localize(datetime.datetime(2014, 4, 21, 9))
start_eastern = start.astimezone(eastern)

start_utc = datetime.datetime(2014, 4, 21, 1, tzinfo=utc)
print(start_utc.strftime(fmt))

start_pacific = start_utc.astimezone(pacific)

print(start)
print(start_eastern)
print(start_utc)
print(start_pacific)
print('\n')
print(apollo_13_naive)
print(apollo_13_eastern)
