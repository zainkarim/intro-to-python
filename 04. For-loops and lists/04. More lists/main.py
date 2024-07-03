x = 5
y = x
print(x) # 5
y = y + 2
print(y) # 7
print(x) # 5

x = ["a", "b", "c"]
y = x
y[0] = "d"
print(y) # [d, b, c]
print(x) # [d, b, c]

# With lists, when you change y you also change x
# Lists and more complex data structures are stored
# differently than int, string, booleans, etc.

x = 5
# In memory somewhere is a cabinet labeled x with the number 5 in it

x = ["a", "b", "c"]
# With a list, you're storing an address to a list.
# x is associated with the address to the list, not the list itself

y = x
# y is being assigned the address associated with the same list
# associated with x. If we make changes to x, then y changes as well, and vice-versa.