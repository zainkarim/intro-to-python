print("Hello World.")

# Order of events:
#   1. Reads line of code
#   2. Interprets instructions
#   3. Executes the instruction
#   4. Implements program counter and repeats until done.
print("My")
print("name")
print("is")
print("Inigo")
print("Montoya")

# Defining a function:
#   1. a header (def ... ):
#   2. A body
def say_introduction():
    print("My name is Inigo Montoya.")

def threaten_vengeance():
    print("You killed my father.")
    print("Prepare to die.")

print("Hello.")
say_introduction() # call say_introduction function
threaten_vengeance() # call threaten_vengeance function

# Abstraction hides the details of how things work and makes it easier to make changes.
say_introduction()
threaten_vengeance()
say_introduction()
threaten_vengeance()

# We can use functions that someone else wrote
from simplefunctions import print_date_and_time #imported a predefined function from the simplefunctions.py file

print_date_and_time()

# In these examples, we can pass parameters to a function
from simplefunctions import print_sqrt 

print_sqrt(4) # call the function
print_sqrt(9)
print_sqrt(26)

# Drill:
def goodbye():
    print("Goodbye")
def hello():
    print("Hello")
    goodbye()
hello()