# HashMap (aka dict)
myMap = {}
myMap["allice"] = 88
myMap["bob"] = 77

print(myMap)
print()

# Taking the length gives you the number of keys in the hash map
print(len(myMap))

myMap["allice"] = 80
print(myMap["allice"])

# O(c) constant time
print("allice" in myMap)

myMap.pop("allice")
print(myMap)

myMap = {"Logan": 20, "Ava": 19}
print(myMap)
print()


# Dict Comprehension
myMap = {i: 2*i for i in range(3)}
print(myMap)
print()

# Looping through Maps
myMap = {"Logan": 20, "Ava": 19}
for key in myMap:
    print(key, myMap[key])
print()

for val in myMap.values():
    print(val)
print()

# Using unpacking
for key, val in myMap.items():
    print(key, val)
