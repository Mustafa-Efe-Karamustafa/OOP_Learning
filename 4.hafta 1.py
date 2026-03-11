import math
class Yardimcilar:

    @staticmethod
    def sinus(x):
        return math.sin(x)

    @staticmethod
    def cos(x):
        return math.cos(x)

    @staticmethod
    def tan(x):
        return math.tan(x)

class Math:
    liste = []
    def sinus(self,x):
        my_value = Yardimcilar.sinus(x)
        Math.liste.append(my_value)
        print(Math.liste)

    def cos(self,x):
        my_value = Yardimcilar.cos(x)
        Math.liste.append(my_value)
        print(Math.liste)

    def tan(self,x):
        my_value = Yardimcilar.tan(x)
        Math.liste.append(my_value)
        print(Math.liste)

a = Math()
b = Math()
c = Math()

a.sinus(1)
b.cos(2)
c.tan(3)






