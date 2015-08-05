def stringcases(string):
  upcase = string.upper()
  lowcase = string.lower()
  titlecase = string.title()
  reverse = string[::-1]
  revjoin = ('').join(reverse)
  gathered = upcase, lowcase, titlecase, revjoin
  return gathered

print(stringcases("this is a string"))
