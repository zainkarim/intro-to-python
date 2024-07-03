"""
x = 5 should be read as
'x is assigned to the value 5' and not as
'x equals 5.' This is because variables can
be reassigned.
"""
x = 5
y = 6
x = 4 # x has been reassigned to 4 and is no longer assigned to 5
z = x + 1
print(z) # 5

x = 5
print(z) # still 5!
# x has been reassigned the value of 5,
# however z has NOT been reassigned.
# z is not x + 1 as it has no memory of that. z is simply a number now

z = x + 1
print(z) # now z = 6

x = 5
y = 6
x = 4
x = x + 1
print(x) # 5