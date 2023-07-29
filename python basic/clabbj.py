class dev:
    a = 12
    b = 13

    def krish(self):
        print("ans:-  ", self.a + self.b)

    def __init__(self, i):  # const.
        print("in const . i s:-  ", i)
class krish(dev):



a = dev(10)  # obj=classname()//it calls the constructor
a.a = 20
a.b = 25
a.krish()
