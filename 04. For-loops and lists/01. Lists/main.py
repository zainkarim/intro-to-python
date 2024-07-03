# A list is a data structure for combining information that you
# may want to be contained in a single variable

# The 7 moons of Jupiter
moons1 = "Io"
moons2 = "Europa"
moons3 = "Ganymede"
moons4 = "Callisto"
moons5 = "Iapetus"
moons6 = "Ione"
moons7 = "Tethys"

# Create and initialize a list
moons = ["Io", "Europa", "Ganymede", "Callisto", "Iapetus", "Ione", "Tethys"]

# Print a few lines from the list
print("Jupiter's first moon is " + moons[0] + ".")
print("Jupiter's second moon is " + moons[1] + ".")

# Print the entire list
print(moons)

# A list can contain anything
numbers = [3, 7, 42, 19, 26]
print(numbers)

# A list can be empty
nothing = []
print(nothing)

# Change an element in a list
characters = ["Horton", "Lorax", "Mayzie"]
print(characters)
characters[1] = "Grinch"
print(characters)

# Change an element in the list using a mathematical expression
characters[5 * 2 - 9] = "Lorax"
print(characters)

# Change an element in the list using a variable
x = 1
characters[x] = "The Cat in the Hat"
print(characters)

# Use list elements as variables
some_numbers = [2, 4, 8, 12]
some_numbers[0] = some_numbers[2] + some_numbers[3]
print(some_numbers) # [20, 4, 8, 12]

# Be careful when accessing your lists!
# print(some_numbers[4]) # ERROR: Does not exist

# The length of a list
x = len(some_numbers)
print("The length of the list \"some_numbers\" is " + str(x) + ".")