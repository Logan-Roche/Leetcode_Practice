# If statements don't need parentheses or curly braces

n = 1 
if n > 2:
    n -= 1
elif n == 2: 
    n *= 2
else:
    n += 2


# Parentheses are needed for muli-line conditions

n, m = 1, 2

if((n > 2 and
    n!=m ) or n == m):
    n += 1

# while loops

n = 0
while n < 5:
    print(n)
    n += 1

# for loops

# loop from i = 0 to i = 4

# not inclusive
for i in range(5):
    print(i)

# 2 to 6 (not inclusive for 6)
for i in range(2, 6):
    print(i)

# Decreatment from i = 5 to i = 2
for i in range( 5, 1, -1):
    print(i)



    
