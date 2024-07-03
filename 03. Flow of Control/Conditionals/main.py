# Conditionals

# Compute the whole number factors of a number:
num = 42
list = []
i = 1
while (i <= num):
    if (num % i == 0):
        list.append(i)
    i += 1
print(list)

# Temperature
temp = 72
if temp <= 32:
    print("It's freezing in here!")
elif temp > 32 and temp <= 50:
    print("It's pretty cold")
elif temp > 50 and temp <= 70:
    print("It's a little chilly")
elif temp > 70 and temp <= 85:
    print("It's warm in here")
else:
    print("It's so hot!")

# Positive/Negative
n = -3
if n > 0:
    print(str(n) + " is positive.")
    n = -1 * n
elif n < 0:
    print(str(n) + " is negative.")
else:
    print(str(n) + " equals 0.")






# Find all whole number factors of a number

num = 1000
i = 1
list = []

while i <= num:
    if num % i == 0:
        list.append(i)
    i += 1

print("The whole number factors of " + str(num) + " are: " + "\n" + str(list))












