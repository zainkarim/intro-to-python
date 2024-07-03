# While Loop
"""
while condition:
    body

The condition is an expression that evaluates to a boolean value (true/false)
"""

# Conditional operators
x = 5
print(x < 5) # False

x = 5
x = x - 2 # x = 3
print (x < 4) # True, 3 is less than 4

c = 5 < 6
print(c) # True? or Error. I think it may be True. It is True
# c is assigned the statement "5 is less than 6,"" which is a conditional statement.
# The statement is true, thus c is true.

x = 5
print(x == 4) # Is x = 4? No, so the output is False
# print(x = 5) # This result in an error, as x = 5 is an assignment that cannot be printed.

# While Loop
t = 0
while(t < 180):
    t = t + 10
    print(t)
# What's happening here? We gave t an initial value of 0.
# We tell the computer to add 10 to the value given to t
# and then print the new value assigned to t over and over until t is 180.
# The loop stops iterating once the instructions result in a value that is higher than 180.