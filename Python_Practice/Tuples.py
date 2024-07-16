# Tuples are like arrays but immutable

tup = (1, 2, 3)
print(tup)
print(tup[0])
print(tup[-1])
print()

# Cannot modify
# tup[0] = 3 <-- this does not work

# Can be used as keys for Hash map/set

myMap = {(1,2): 3}
print(myMap)
print()

mySet = set()
mySet.add((1,2))
print(mySet)
print((1,2) in mySet)
print()

#Lists cannot be keys
# myMap[[3, 4]] = 5 <--- cannot do this

