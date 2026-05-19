from pathlib import Path
import os
print(type(Path.cwd()))
var = Path.cwd()
print(var)
print(str(var))

var = var / '..'
print(var)
os.chdir(var)
print(Path.cwd())
print(Path.home())
os.chdir(Path.cwd() / 'Python-automate-boring stuff')
print(Path.cwd())
os.makedirs('test')
