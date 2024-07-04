# --- DRILL ---
# Write a class named Kangaroo with:
# 
# constructor: initializes an instance variable
# named "pouch_contents" to an empty list.
# 
# put_in_pouch: takes a string as input and adds
# it to pouch_contents, if it is not already in
# the pouch. If it IS already in the pouch, print
# "object already in pouch"
# 
# __str__: prints content of pouch. If pouch is empty
# then print "The pouch is empty." If the pouch is 
# not empty then print "The kangaroo's pouch contains: 
# [A, B, C]" where A, B, C are the contents of the pouch
# 
# Write a short driver to test your class

class Kangaroo:
    def __init__(self):
        self.pouch_contents = []
    
    def __str__(self):
        if self.pouch_contents == []:
            return "The pouch is empty."
        else:
            return "The kangaroo's pouch contains: " + str(self.pouch_contents)
        
    def put_in_pouch(self, item):
        if item in self.pouch_contents:
            print(item + " is already in the pouch!")
        else:
            self.pouch_contents.append(item)           
            
joey = Kangaroo()
print(joey)

joey.put_in_pouch("Bob")
print(joey)

joey.put_in_pouch("Bob")
joey.put_in_pouch("Billy")
print(joey)
