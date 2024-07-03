"""
Write a recursive function that takes as input a list of integers and returns the sum of all even numbers in the list. If the list is empty, return 0 (hint: this is your base case).

Write a recursive function that takes as input a string and returns True if it is a palindrome and False if it is not. A string of length 0 or 1 is a palindrome. A string of length greater than 1 is a palindrome if the first and last character are the same, the second and second to last character are the same, etc.

Your solution to each part may not use any for- or while-looping constructs.
"""

def sum_even_recursive(list):
    if list == []:
        return 0
    else:
        if list[0] % 2 == 0:
            return list[0] + sum_even_recursive(list[1:])
        else:
            return sum_even_recursive(list[1:])
        
nums = [1, 2, 3, 4, 5, 6]
print(sum_even_recursive(nums))

def is_palindrome_recursive(string):
    # Base case:
    if len(string) == 0 or len(string) == 1:
        return True
    # Recursive case
    else:
        if string[0] == string[len(string) - 1]:
            is_palindrome_recursive(string[1:])
            return True
        else:
            return False
        
string = "racecar"
print(is_palindrome_recursive(string))