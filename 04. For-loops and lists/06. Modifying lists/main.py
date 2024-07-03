# Lists are stored as addresses
def reverse_list(L):
    for i in range (0, int(len(L) / 2)):
        j = int(len(L) - 1 - i)
        temp = L[i]
        L[i] = L[j]
        L[j] = temp

list_a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(list_a)
# The address of list is passed in to the function
reverse_list(list_a)
print(list_a)

list_b = [2, 4, 6, 8, 10, 12, 14, 16, 18]
# These two variables point to the same address in memory
new_list = list_b
reverse_list(new_list) # new_list and list_b will both be reversed
print(new_list)
print(list_b)

list_c = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
copy_list = list(list_c) # make a copy at a different address in memory
reverse_list(copy_list)
print(copy_list) # This will be reversed
print(list_c) # This will not be reversed

# This notion of storing lists as objects is incredibly important

### More list commands

# Sorting a list
unis = ["TAMU", "UT", "UTD", "UTA", "UNT", "TTU", "SFA", "BU", "TWU"]
alphabetized_unis = sorted(unis)
print(alphabetized_unis)

# Appending to a list
nums = [1, 2, 4, 5, 6, 7, 8, 9]
nums.insert(2, 3) # (index, object)
nums.append(10) # Adds to end of list
print(nums)

# Deleting from a list
del nums[0]
print(nums)

# ——— DRILL ———-
# write some code that computes the length and
# position of the largest list in a list of lists

# 1. Look at the length of the list in the first index
# 2. Look at the length of the list in the second index
# 3. If the length of the list in the second index is longer,
#    update longest_list to the second index.
# 4. Keep going until we reach the end of the list.

L = [[1,2,3],[11,12,13,14,15,16],[4,5,6,7],[8,9],[10]]

longest_list = 0
list_length = 0
for i in range (0, len(L)):
    if(len(L[i]) > len(L[longest_list])):
        longest_list = i
        list_length = len(L[i])
    else:
        i += 1

print("The longest list is located at index " + str(longest_list) + 
      " and has a length of " + str(list_length) + ".")