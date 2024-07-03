from math import pi, sin

print(pi) # 3.141592....

print(sin(pi)) # 1.22e-16

print(sin(pi) == 0) # False? Why?

# Using the equality operator on floating point values leads to some measurement error.
# Pi is an infinite number which is being represented in a finite space on the computer.
# This is why Python interprets sin(pi) as a really small number that is close to zero,
# but not actually zero.

# Logical Operators
# A and B: True is A is True and B is True
# A or B: True if A or B is True
# not(A): True if A is False, False if A is True ; Basically just inverting
not((3 < 4) and (10 < 12)) # False
(10 > 12) or (5 != 6) # True
not(not(False == False)) # True
True > False # True = 1, False = 0, True
"aardvark" < "zebra" # True, a is a lower ASCII value than Z

# Short Circuiting
x = 0
print((x != 0) and (3/x < 4)) # False
print((3/x < 4) and (x != 0)) # Division by zero error
# If you're evaluating a series of 'ands' and any of them are false,
# Python skips the rest of the series and evaluates the whole thing is False.
# Python reads the code from left to right. In the second example, the first expression evaluates to True, so Python has to continue to evaluate the second expression.
