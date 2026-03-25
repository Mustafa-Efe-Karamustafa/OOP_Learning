from abc import ABC, abstractmethod
import math
import random
import matplotlib.pyplot as plt

class Trigonometry:


    @abstractmethod
    def get_value(self,value):
        pass

    def __del__(self):
        pass



class Sinus(Trigonometry):

    def __str__(self):
        return "Sin"

    def get_value(self,value):
        return math.sin(value)

class Cos(Trigonometry):

    def __str__(self):
        return "Cos"

    def get_value(self,value):
        return math.cos(value)

class Tan(Trigonometry):

    def __str__(self):
        return "Tan"

    def get_value(self,value):
        return math.tan(value)


'''
my_dict = {}
geo_list = [Sinus(),Cos(),Tan()]

for i in range(3):
    my_dict[str(geo_list[i])] = geo_list[i].get_value(i)
print(my_dict)
'''

x_list = []
y_list = []
geo_list = [Sinus(),Cos(),Tan()]
for i in range(365):
    new_i = random.randint(0,365)
    idx = random.randint(0,len(geo_list)-1)
    x_list.append(new_i)
    y_list.append(geo_list[idx].get_value(new_i))


for i in range(0,len(y_list)-1):
    for j in range(i+1,len(y_list)):
        if x_list[i] > x_list[j]:
            y_list[i],y_list[j] = y_list[j],y_list[i]
            x_list[i],x_list[j] = x_list[j],x_list[i]

print(x_list)
print(y_list)




plt.plot(x_list,y_list)
plt.xlabel("x")
plt.ylabel("y")
plt.show()


