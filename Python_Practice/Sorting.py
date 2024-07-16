# Sorting

arr = [5, 4, 7, 3, 8]

arr.sort()
print(arr)

arr.sort(reverse=True)
print(arr)

# sorting Strings
arr = ["bob", "alice", "jane", "doe"]

arr.sort()
print(arr)

# Custom sort (by length of stirng)
arr.sort(key=lambda x: len(x))
print(arr)

