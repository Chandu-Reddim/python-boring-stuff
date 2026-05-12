import re
obj = re.compile(r'\d{3}')
match = obj.search('444 nothing to catch')
print(match.group())
print(type(match))
