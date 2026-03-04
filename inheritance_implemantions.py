import math
import matplotlib.pyplot as plt
class Trigonometry:
    def __init__(self,start,stop,step):
        self.x = []
        self.y = []
        self.start = start
        self.stop = stop
        self.step = step

    def calculate(self):
        pass

    def WriteValues(self):
        print("x",self.x)
        print("y",self.y)

class Sinus(Trigonometry):
    def __init__(self,start,stop,step):
        super().__init__(start,stop,step)

    def calculate(self):
        for i in range(self.start,self.stop,self.step):
            self.x.append(i)
            self.y.append(math.sin(i))

class Cosinus(Trigonometry):
    def __init__(self,start,stop,step):
        super().__init__(start,stop,step)

    def calculate(self):
        for i in range(self.start,self.stop,self.step):
            self.x.append(i)
            self.y.append(math.cos(i))

class Tan(Trigonometry):
    def __init__(self,start,stop,step):
        super().__init__(start,stop,step)
        self.isim = "Tanjant"

    def calculate(self):
        for i in range(self.start,self.stop,self.step):
            self.x.append(i)
            self.y.append(math.tan(i))


class Container:
    def __init__(self,trigonesne=None):
        self.trigo = trigonesne


    def call(self):
        if not (self.trigo == None):
            self.trigo.calculate()

class Bag:
    def __init__(self):
        self.trigolist = []


    def AddObject(self,object):
        self.trigolist.append(object)

    def Call(self):
        for i in self.trigolist:
            i.calculate()
            i.WriteValues()

    def Plot(self):
        for i,val in enumerate(self.trigolist):
            plt.subplot(3,3,i+1)
            plt.plot(val.x,val.y)
        plt.show()





s0 = Sinus(0,50,4)
s1 = Sinus(10,50,2)
c0 = Cosinus(10,70,15)
c1 = Cosinus(25,50,10)
s2 = Sinus(30,50,10)
tn0 = Tan(40,50,5)
tn1 = Tan(15,18,1)

bg = Bag()
bg.AddObject(s0)
bg.AddObject(s1)
bg.AddObject(s2)
bg.AddObject(tn0)
bg.AddObject(tn1)
bg.AddObject(c0)
bg.AddObject(c1)
bg.Call()
bg.Plot()
