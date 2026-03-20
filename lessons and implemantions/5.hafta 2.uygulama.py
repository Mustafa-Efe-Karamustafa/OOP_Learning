class Student:
    def __init__(self,name,age,no):
        self.name = name
        self.age = age
        self.no = no


    def say_yourself_department(self):
        pass

class Industrial(Student):
    def __init__(self,name,age,no):
        print("hello industrial")
        super().__init__(name,age,no)

    def get_department1(self):
        return "industrial department"

    def say_yourself_department(self):
        print("industrial department")
        super().say_yourself_department()


class Computer(Student):
    def __init__(self,name,age,no):
        print("hello computer")
        super().__init__(name,age,no)


    def get_department2(self):
        return "computer department"


    def say_yourself_department(self):
        print("Computer department")
        super().say_yourself_department()



class CAP(Industrial,Computer):
    def __init__(self,name,age,no):
        print("hello CAP")
        super().__init__(name,age,no)

    def get_department(self):
        return f"I am currently working on {self.get_department1()} and {self.get_department2()}"

    def say_yourself_department(self):
        super().say_yourself_department()

o0 = CAP("o0",0,0)

print("mro ---> ",CAP.mro())
print(o0.get_department())
o0.say_yourself_department()
