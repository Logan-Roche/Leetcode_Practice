# HashSet - list that does not contain duplicates

mySet = set()

mySet.add(1)
mySet.add(2)
print(mySet)

print(len(mySet))

print(1 in mySet)
print(3 in mySet)

# Remove values in constant time
mySet.remove(2)
print(mySet)
print(2 in mySet)


# List into a set
print(set([1, 2, 3]))

# Set Comprehension
mySet = {i for i in range(5)}
print(mySet)

