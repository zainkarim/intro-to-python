# --- DRILL ---
# Write a python function, count_evens, that
# takes as input a list of numbers and
# returns the number of even numbers

def count_evens(list):
    num_evens = 0
    for i in list:
        if i % 2 == 0:
            num_evens += 1
    return num_evens

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(count_evens(nums))
