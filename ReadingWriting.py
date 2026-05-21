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
print(p.parts)
print(p.parents[0])
# Parents method does not return a list object to apply slicing so only [number] works and parents method is to get the ancestral path from existing
try:
    print(p.parents[1])
except Exception:
    print("error raised")

p = Path.cwd() / 'test2'
print(f' 0 is {p.parents[0]} and 1 is {p.parents[1]}')

# for D:/a/b 0 - D:/a for 1 - D:/ ( 2  steps lower)

# to get stats of a object
print(p.stat())
print(p.stat().st_file_attributes)