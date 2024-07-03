# --- DRILL ---
# Write an iterative function that takes as input
# integer "n" and returns the sum of the first "n"
# integers: sum(5) returns 1 + 2 + 3 + 4 + 5 = 15

def n_sum(n):
    sum = 0
    for i in range(0, n + 1):
        sum += i
    return sum

print(n_sum(5))

# --- DRILL ---
# Write a recursive function that takes as input
# integer "n" and returns the sum of the first "n"
# integers: sum(5) returns 1 + 2 + 3 + 4 + 5 = 15

def sum_recur(n):
    if n == 0:
        return 0
    else:
        return n + sum_recur(n - 1)
    
print(sum_recur(5))
