# the functin sqrt takes as input a number and RETURNS a number
from math import sqrt
x = sqrt(4)
print(sqrt(4))

# the function "+" takes as input two numbers and RETURNS a number
x = 8 + 12
print(8 + 12)

# the function len takes as input a string and RETURNS an integer
print(len("eggplant"))

# the return value of one function can be the input to another
print(int(8.485) + 12)
print(int(sqrt(72)) + 12)

def compute_four(): # defining a function
    return 24 / 4 - 2 # hand a value back to the calling funtion

x = compute_four()
print(x) # 6

y = 24 / compute_four()
print(y)# 4

print(compute_four()) # 4