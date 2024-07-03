# Write an iterative function that takes as input a list of numbers and sums them all up.
def listSum(list):
    sum = 0
    for i in range (0, len(list)):
        sum += list[i]
    return sum

# Write a recursive function that takes as input a list of numbers and sums them all up.
# Base case; list contains only one item, or list is empty
def mySum(list):
    if(list == []):  # base case : empty list
        return 0
    else:
        return list[0] + mySum(list[1:])
    
list = [1, 2, 3, 4]
print(listSum(list))
print(mySum(list))