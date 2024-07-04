class Student:
    def __init__(self, name, exam_grade, height_in_cm):
        self.name = name
        self.exam_grade = exam_grade
        self.height_in_cm = height_in_cm
    
    def __str__(self):
        return "(" + self.name + ", " + str(self.exam_grade) + ", " + str(self.height_in_cm) + ")"
    
    # add isFailing() function
    def isFailing(self):
        return self.getGrade() < 65
        '''
        # above code is the more concise version of this:
        if self.getGrade() <= 65:
            return True
        '''
    # accessor functions
    def getName(self):
        return self.name

    def getGrade(self):
        return self.exam_grade

    def getHeight(self):
        return self.height_in_cm
    
zain = Student("Zain Karim", 92, 180)
print(zain)

# access a student's info (DON'T DO THIS!)
print(zain.height_in_cm)
print(zain.exam_grade)

# instead, use accessor or getter functions
print(zain.getName())
print(zain.getHeight())
print(zain.getGrade())

student_list = [Student("Alice", 92, 160),
                Student("Bob", 57, 128),
                Student("Grace", 100, 200)]

# print all students
for i in range(0, len(student_list)):
    print(student_list[i]) # calls __str__ in Student class

# print students that are failing (below 65)
for i in range(0, len(student_list)):
    if student_list[i].getGrade() <= 65:
        print(student_list[i].getName())

# Print students that are failing using isFailing():
for i in range(0, len(student_list)):
    if student_list[i].isFailing():
        print(student_list[i].getName())

# print all exam scores in sorted order
def key_grade(student): # not a function of class Student!
    return student.getGrade()

# Use the key command to determine how a list of OBJECTS will be sorted using a predefined function
student_list.sort(key=key_grade)

for i in range(0, len(student_list)):
    print(student_list[i])