# Local vs Global
def some_function():
    x = 4 # assigns x (local variable) inside function body
    print(x)

some_function()
# print(x) # x is not in scope -> undefined

def print_y():
    global y # allows you to modify a global variable
    y += 1 # <-- global var
    print(y)

# y is a global variable, not inside of the print_y function UNLESS made global inside function.
y = 5

print_y() # 6
print_y() # 7

def print_z():
    print(z)

z = 1
print_z() # this works because the function is only READING z, not modifying it.

# Dangerous things that can happen with global variables:
from math import pi
def compute_circle_area(r):
    global pi # make pi globally accessible
    pi = 3 # change the value of pi EVERYWHERE -- not cool!
    return pi * (r ** 2)

compute_circle_area(10)

# It's possible for local and global variables to interfere with each other.
var = 1
def test(x):
    global var # make var globally accessible // which var are you referring to?
    var += 1
    print(var)

test(10)