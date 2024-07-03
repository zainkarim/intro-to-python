def add_five(x):
    x += 5
    return x

z = 4
add_five(z)
print(z) # 4

x = add_five(z)
print(x) # 9

print(add_five(z)) # 9

def return_something(x):
    if(x > 0):
        return 1
    else:
        return -1
    
def print_something(x):
    if(x > 0):
        print(1)
    else:
        print(-1)

y = print_something(12)
print(y) # None. the print_something function does not return a specific value.

from random import uniform

def cheap_magic_8_ball():
    r = uniform(0,4)

    if r > 3:
        print("Most likely")
    elif r > 2:
        print("Ask again later")
    elif r > 1:
        print("Don't count on it")
    else:
        print("No")

cheap_magic_8_ball()

def cheap_magic_8_ball_2():
    r = uniform(0,4)

    if r > 3:
        return "Most likely"
    elif r > 2:
        return "Ask again later"
    elif r > 1:
        return "Don't count on it"
    else:
        return "No"

print(cheap_magic_8_ball_2()) # this method of outputting data is preferable

def return_two_things(x,y):
    sum = x + y
    product = x * y
    return(sum,product) # nothing can follow this return statement

(s,p) = return_two_things(2, 5)
print(s,p)

def isPrime(x): 
    for i in range(2, x - 1):
        if x % i == 0:
            return(print(str(x) + " is not a prime number."))
        else:
            i += 1
    return (print(str(x) + " is a prime number."))

isPrime(11)

