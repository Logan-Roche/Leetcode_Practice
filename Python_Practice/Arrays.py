# Arrays (called lists in python)
arr = [1, 2, 3]
print(arr)

# can be used as stack
arr.append(4)
arr.append(5)
print(arr)

arr.pop()
print(arr)

# inserting is Big Oh of N time
arr.insert(1, 7)
print(arr)

# Indexing an array is constant
arr[0] = 0
arr[3] = 0