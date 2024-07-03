# Reverse this list
L = ["a", "b", "c", "d", "e", "f"]

# 1. Swap the first and last elements
# 2. Swap the second and second to last elements
# 3. Swap the third and third to last elements

# for first half (round down) of
# items in list:
#   swap item with corresponding
#   item at end of list

for i in range(0, int(len(L)/2)):
    temp = L[i] # this is necessary to hold the value
                # that is reassigned without losing it
    L[i] = L[len(L) - (i + 1)]
    L[len(L) - (i + 1)] = temp


print(L)

# Check if a string is a palindrome

string = "racecar"

isPalindrome = True
for i in range(0, int(len(string)/2)):
    if string[i] != string[len(string) - (i + 1)]:
        isPalindrome = False
        print("\"" + string + " is not a palindrome.")
        break

if(isPalindrome):
    print("\"" + string + "\" is a palindrome.")

# --- DRILL ---
# Write some code that prints "has22" if
# the list contains a 2 next to a 2 anywhere in
# the list, and returns "no22" otherwise
# hint: use the break command in the for loop
# hint: similar to prime number example.
# You're looking for something, and if you don't find it, THEN you have to print something

nums = [1, 2, 3, 4, 5, 6, 3, 2, 1, 6, 3, 5 , 7, 8,]

# 1. Check number at [i]. If number at [i] is 2, then hold on to it.
# 2. Compare to next number. If next number is also 2, break and print "has22"
# 3. If next number is not 2, keep going until another 2 is found and hold onto that index.
# 4. Step 2 again, if not then step 3 again, if end of list is reached then print "no22"

# Start by just trying to print "has22"
# Once that works, figure out how to only do it once if there's more than one pair of 2s
# Then try to print "no22"

has22 = 0
for i in range(0, len(nums)):
    if (nums[i] == 2 and nums[i + 1] == 2):
        has22 = 1
        print("has22")
        break

if(has22 == 0):
    print("no22")