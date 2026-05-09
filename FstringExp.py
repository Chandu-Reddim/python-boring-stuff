import dis
name="Kenzo"
def formatVsFstring():
    print("hello {}".format(name))
    print(f"hello {name}")

dis.dis(formatVsFstring)

'''F string are better than format string as it has no function call and praser takes care of '''
gender=5
height=5.656357
precision=2
id=777
print(f'Hello {height:{precision}.0f}')
print(f"My height is {height:{10}.{0}f}") #with 10 precision it creating a distance from before character
print(f"Hello {name=}")
print(f"hello {id!s}")
#print(f"hello {}")