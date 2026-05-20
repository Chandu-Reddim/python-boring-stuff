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
os.makedirs('test',exist_ok=True)
print(os.listdir())
print(os.getcwd())
Path(Path.cwd(),'test2').mkdir(parents=True,exist_ok=True)
print(os.listdir())
print(Path.cwd().is_absolute())
print((Path.cwd() / 'test2').is_absolute())
print(Path('test2').absolute())
p = Path.cwd()
print(f'Parent is {p.parent} and drive is {p.drive} , anchor is {p.anchor}, name is {p.name}, stem/base is {p.stem} and suffix is {p.suffix}')