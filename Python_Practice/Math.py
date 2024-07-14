import math
# Division is decimal by default

print(5/2)

# Double slash rounds down
print(5//2)

# CAREFUL: most languages roundtowards 0 by default so negative numbers will round down
print(-3 // 2)

# A work around for rounding towards zero is to use decimal division and then convert to int
print(int(-3 / 2))

# modding is similar to most languages
print(10 % 3)

# Except for negative
print(-10 % 3)

# Math Helpers
print(math.floor(3 / 2))
print(math.sqrt(3 / 2))
print(math.pow(2, 3))

# Max / Min int

float("inf")
float("-inf")

# Python nnumbers are infinite so tehy do not overflow
print(math.pow(2, 200))
