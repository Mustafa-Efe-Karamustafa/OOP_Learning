from abc import ABC, abstractmethod
import math
import random
import matplotlib.pyplot as plt

class Trigonometry(ABC):

    @abstractmethod
    def get_value(self,x):
        pass

class Sinus(Trigonometry):

    def get_value(self,x):
        return math.sin(x)

class Cos(Trigonometry):

    def get_value(self,x):
        return math.cos(x)

class Tan(Trigonometry):

    def get_value(self,x):
        return math.tan(x)

class CotTan(Trigonometry):

    def get_value(self,x):
        return 1 / math.tan(x)


class Bag():

    trigon_list = []
    x_list = []
    y_list = []

    @classmethod
    def create_list(cls,value):
        cls.trigon_list.append(value)

    @staticmethod
    def get_value_and_bag_value(num:int):
        random.seed(42)
        for i in range(0,num):
            x = random.randint(0,365)
            Bag.x_list.append(x)
            idx = random.randint(0,len(Bag.trigon_list)-1)

            Bag.y_list.append(Bag.trigon_list[idx].get_value(x))
    @staticmethod
    def sort_all_thing():
        for i in range(0,len(Bag.x_list)-1):
            for j in range(i+1,len(Bag.y_list)):
                if Bag.x_list[i] > Bag.x_list[j]:
                    Bag.x_list[i],Bag.x_list[j] = Bag.x_list[j],Bag.x_list[i]
                    Bag.y_list[i],Bag.y_list[j] = Bag.y_list[j],Bag.y_list[i]


    @staticmethod
    def write_plot():
        plt.plot(Bag.x_list,Bag.y_list)
        plt.xlabel("x")
        plt.ylabel("y")
        plt.show()

for i in [Sinus(),Cos(),Tan(),CotTan()]:
    Bag.create_list(i)

Bag.get_value_and_bag_value(15)
Bag.sort_all_thing()
Bag.write_plot()

'''
trigo_list = [Sinus(),Cos(),Tan(),CotTan()]
x_list = []
y_list = []
random.seed(42)
for i in range(100):
    idx = random.randint(0,len(trigo_list)-1)
    x = random.randint(0,365)
    x_list.append(x)
    y_list.append(trigo_list[idx].get_value(x))

for i in range(0,len(x_list)-1):
    for j in range(i+1,len(x_list)):
        if x_list[i] > x_list[j]:
            x_list[i],x_list[j] = x_list[j],x_list[i]
            y_list[i], y_list[j] = y_list[j], y_list[i]

plt.plot(x_list,y_list)
plt.xlabel("x")
plt.ylabel("y")
plt.show()
'''

