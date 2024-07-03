# lists and loops
nums = [1, 7, 4, 10, 8]
i = 0
while(i < len(nums)):
    if(nums[i] % 2 == 0):
        print(str(nums[i]) + " is even")
    else:
        print(str(nums[i]) + " is odd")
    i += 1

# for loop
for i in range(1, 11): # notice that we have to add 1 to the range
    print(i)

for i in range(0, len(nums)):
    if(nums[i] % 2 == 0):
        print(str(nums[i]) + " is even")
    else:
        print(str(nums[i]) + " is odd")

for n in nums: # n takes on the values instead of the index
    if(n % 2 == 0):
        print(str(nums[i]) + " is even")

# Strings can be treated like lists (sort of)
mystring = "Chevy!"
for c in mystring:
    print(c)

# but this doesn't work
# mystring[0] = "c"
    
# a list can contain multiple data types
mixed_list = [1, "abc", True, 2.0]

# including lists
mixed_list = ["abc", [3, 2, 1]] # This list contains two elements,
                                # one of which is a list with three elements.
                                # This is called a 2D list
L = mixed_list[1] # L has been assigned to the item in mixed_list[1]
                  # L = [3, 2, 1]
print(L) # [3, 2, 1]
print(L[0]) # 3
print(mixed_list[1][0]) # 3