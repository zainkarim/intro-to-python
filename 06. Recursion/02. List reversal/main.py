# iterative list reversal:

def reverse_list(list):
    for i in range(0, int(len(list) / 2)):
        temp = list[i]
        list[i] = list[len(list) - 1 - i]
        list[len(list) - 1 - i] = temp
        i += 1
    return list

list = [1, 2, 3, 4, 5]
print(reverse_list(list))

def reverse_string(word):
    reversed_string = ""
    for char in word:
        reversed_string = char + reversed_string
    return reversed_string

word = "hello"
print(reverse_string(word))

# Recursive string reversal:
'''
reverse("ward") = "draw"
reverse("ward") = reverse("ard") + "w"          = "draw"
    reverse("ard") = reverse("rd") + "a"        = "dra"
        reverse("rd") = reverse("d") + "r"      = "dr"
            reverse("d") = "d"                  = "d"
'''
def reverse(s):
    if len(s) == 1: # base case
        return s
    else:
        return reverse(s[1:len(s)] + s[0])