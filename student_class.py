class StudentClass:
    firstname = "dileep"
    lastname = "kumar"
    roll_number = 15731
    age = 16
    study = "s.s.c"
    marks = 74

    if marks >= 75:
        print("student :", "good")
    elif marks >= 35:
        print("student:", "pass")
    else:
        print("student :", "fail")

    def get_fullname(self):
        return self.firstname + self.lastname

    def get_firstname(self):
        return self.firstname

    def get_lastname(self):
        return self.lastname

    def get_age(self):
        return self.age

    def get_roll_number(self):
        return self.roll_number

    def get_study(self):
        return self.study

    def get_marks(self):
        return self.marks



student_class_object = StudentClass()
result = student_class_object.get_fullname()
print(result)

result = student_class_object.get_firstname()
print(result)
result = student_class_object.get_lastname()
print(result)
result = student_class_object.get_roll_number()
print(result)
result = student_class_object.get_age()
print(result)