class Student:
    number_of_students = 0
    student_list = []


    def __init__(self, name, age):
        self.name = name
        self.age = age
        Student.number_of_students += 1
        Student.student_list.append(self)


    @classmethod
    def create_student(cls, name, age):
        return cls(name, age)


    def __str__(self):
        return f'{self.name} {self.age}'

    @classmethod
    def write_values(cls,value:list):
        for i in value:
            print(i)



o0 = Student.create_student("Efe", 19)
o1 = Student.create_student("Tunahan", 17)



print(Student.number_of_students)
print(Student.student_list)
Student.write_values(Student.student_list)


