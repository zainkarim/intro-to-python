from random import uniform

def magic_8_ball():
    r = uniform(0, 4) # A random uniformally distributed
                      # floating point number between 0 and 4.
    print(r)

    if(r <= 1):
        print("Most likely.")
    elif(r <= 2):
        print("Ask again later.")
    elif(r <= 3):
        print("Don't count on it.")
    else:
        print("No.")

magic_8_ball()