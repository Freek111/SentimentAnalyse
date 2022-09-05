import re

print(re.findall('abc', 'kasdfaiabcasdfaabc'))

iterator = re.finditer('abc', 'kasdfaiabcasdfaabc')
for match in iterator:
    print(match.group())