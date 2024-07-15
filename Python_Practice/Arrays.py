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

# Initlizing arr of size n with eefault value of 1

n = 5

arr = [1] * n

print(arr)
print(len(arr))

# Careful: -1 is not out of bounds, it's the last value
arr = [1, 2, 3]
print(arr[-1])
print(arr[-2])

# Sublists (aka Slicing)
arr = [1, 2, 3, 4, 5]

print(arr[1:3])

# Unpacking arrays into variables
a, b , c = [1, 2, 3]

print(a, b, c)

# Loop through arrays
nums = [1, 2, 3]

for i in range(len(nums)):
    print(nums[i])

# Without Indexing
for n in nums:
    print(n)

# With index and value
for index, value in enumerate(nums):
    print(index , value)
print()


# loops through multiple arrays simultaneously with unpacking
nums1 = [1, 3, 5]
nums2 = [2, 4, 6]

for n1, n2 in zip(nums1, nums2):
    print(n1, n2)
print()

# Reversing
nums = [1, 2, 3]

nums.reverse()
print(nums)



