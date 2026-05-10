print('-'.join(['a','b','c','c']))
# join adds the - with every parameter provided.
# join works quicker than the for loop and concetenation with + as it leads to creating many intermediate strings along the way
print('hello'.rjust(10,'='))
print('hello'.center(10,'='))
print('hello github and I am not github'.split())
print('abcbbcbcbccababcGITHUBbcbacbc'.strip('abc'))
#as you see it removes any character passed and stop when it find a character that not passed as an parameter
print('abcbbcbcbccababcGITHUBbcbacbc'.rstrip('abc'))
print('abcbbcbcbccababcGITHUBbcbacbc'.lstrip('abc'))
print(ord('a'))
print(ord('A'))
print(chr(65))

import timeit
setup_code='filename="script.sh"'
#filename='script.py'

test_or='filename.endswith(".py") or filename.endswith(".txt") or filename.endswith(".sh")'

test_tuple='filename.endswith((".py",".txt",".sh"))'

time_or=timeit.timeit(test_or,setup=setup_code,number=5000000)
time_tuple=timeit.timeit(test_tuple,setup=setup_code,number=5000000)

print(f"time for or is {time_or:.{2}f} and for the tuple is {time_tuple:.{2}f}")

#with tuple it works faster but keep in mind that due to short circuit evaluation or can be quicker if first or happens to be true it did not check for next.