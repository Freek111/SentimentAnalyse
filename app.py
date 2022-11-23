import re

doc = r'\n for new [line 1, ] \section 3 and \document_ and_ \\\section \n'

regex = '[ \d_]'

print(len(re.findall(regex, doc)))