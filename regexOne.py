import re
obj = re.compile(r'\d{3}')
match = obj.search('44444 nothing to catch')
print(match.group())
print(type(match))
match2 = obj.search('nothing to search')
try:
    if match2 == None:
        print('it is none type')
    print(match2.group())

except BaseException:
    print(type(match2))

matched3 = obj.search('111 2222 3333')
print(matched3.group())

escape = re.compile(r'\(\d{3}\)')
macthed4 = escape.search('(122)')
print(macthed4.group())

matched5 = escape.search('(123)4')
matched6= escape.search('(1225)')

try:
    print(matched5.group())
    print(matched6.group())
except BaseException:
    print(type(matched5))
    print(type(matched6))

print('Now lets learn about the alternating matches')
alt = re.compile(r'ho(me|st|use)')
altMatched = alt.search('Our home is not a host for mosquitoes')
print(altMatched.group())
print(altMatched.groups())
print(altMatched.group(1))

print('lets start grouping')
phone_re = re.compile(r'(\d\d\d)-(\d\d\d)-(\d\d\d\d)')
groups1 = phone_re.search('333-333-4444 hello 111-222-4444')
print(groups1.group())
print(groups1.group(0))
print(groups1.group(1))
print(groups1.groups())

groups2 = phone_re.findall('333-333-4444 hello 111-222-4444')
print(type(groups2))
print(groups2)
print(dir(groups2))

## does over lap matches with search

overlap = re.compile(r'\d{3}')
matched = overlap.search("123456\n111111")
print(matched.group())
print(overlap.findall('123456\n111222'))

# find all with groups 
phone_re = re.compile(r'(\d\d\d)-(\d\d\d)-(\d\d\d\d)')
print(phone_re.findall('333-333-4444 hello 111-222-4444 123'))
