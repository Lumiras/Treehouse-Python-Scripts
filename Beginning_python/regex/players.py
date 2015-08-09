import re

string = '''Love, Kenneth: 20
Chalkley, Andrew: 25
McFarland, Dave: 10
Kesten, Joy: 22
Stewart Pinchback, Pinckney Benton: 18'''

players = re.search(r'''
  (?P<last_name>[\w]+\s?[\w]+?)
  ,\s
  (?P<first_name>[\w]+\s?[\w]+?)
  :\s
  (?P<score>[\d]+)
  ''', string, re.M|re.X)

print(players)
