import re

x = '72314ab4621acd&+*!'

test = re.findall('\d\d\d\d',x)

print(test)