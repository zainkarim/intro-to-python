# ———DRILL ———
# Write some code to determine if a number is prime.
# Print either “not prime” or “is prime”. A number is 
# prime if the only integer divisors are 1 and itself

num = 9
i = 2

while(i < num):
    if(num % i == 0):
        print(str(num) + " is not a prime number.")
        break
    else:
        i += 1

if(i == num):
    print(str(num) + " is a prime number.")