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

