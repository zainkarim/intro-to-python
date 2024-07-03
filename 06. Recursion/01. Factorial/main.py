"""
Factorial:
if n == 0:
    n! = 1
if n > 0
    n! = n * (n - 1) * (n - 2) * ... * 1
"""

def factorial_iterative(n):
    factorial = 1 # initialize factorial value
    i = 1 # start counter
    while i <= n: #while counter is less than n
        factorial *= i # factorial * counter = factorial (1 * 1 = 1, 1 * 2 = 2, 2 * 3 = 6, etc.)
        i += 1
    return factorial

print(str(factorial_iterative(5)) + " (iterative)")

'''
1   = 1 * 1  = 1!
2   = 2 * 1! = 2!
6   = 3 * 2! = 3!
24  = 4 * 3! = 4!
120 = 5 * 4! = 5!

Therefore...

Factorial:
if n == 0:
    n! = 1
if n > 0
    n! = n * (n - 1)!
'''

def factorial_recursive(n):
    if n == 0:
        return 1
    else:
        return n * factorial_recursive(n - 1) # calling the function recursively!
    
print(str(factorial_recursive(5)) + " (recursive).")
        