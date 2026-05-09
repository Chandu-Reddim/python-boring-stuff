import dis
name="Kenzo"
def formatVsFstring():
    print("hello {}".format(name))
    print(f"hello {name}")

dis.dis(formatVsFstring)