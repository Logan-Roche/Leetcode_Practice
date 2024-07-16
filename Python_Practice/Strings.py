# Strings are similar to arrays
s = "abc"

print(s[0:2])

# But they are immutable
# s[0] = a <-- cannot do this

# adding to string creates new string and is O(n) time
s += "def"
print(s)

# Valid numeric string can be converted
print(int("123") + int("123"))

# and numbers can be convered to strings
print(str(123) + str(123))

# Need the ASCII value of a char
print(ord("a"))
print(ord("b"))

# Combine a list of strings( with an empty string delimitor)
strings = ['ab', 'cd', "ef"]
print("".join(strings))
