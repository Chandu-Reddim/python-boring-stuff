import pyperclip

content = pyperclip.paste()
#print(type(content))
#print(content)
dup = content.split('\n')
#print(dup)
content = content.split('\r')
content = ['* '+conten.strip('\n')  for conten in content ]
content = '\n'.join(content)
print(content)
pyperclip.copy(content)

