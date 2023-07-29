class number:
    def __init__(self, num):
        self.num = num

    def __add__(self, n2):
        print("let's add")
        return self.num + n2.num

    def __mul__(self, n2):
        print("let's multiply")
        return self.num * n2.num

    def __sub__(self, n2):
        print("let's subtract")
        return self.num - n2.num

    def __truediv__(self, n2):
        print("let's divide")
        return self.num / n2.num

    def __floordiv__(self, n2):
        print("let's floor divide")
        return self.num // n2.num

    def __pow__(self, n2, modulo=None):
        print("let's power")
        return self.num ** n2.num


n1 = number(7)
n2 = number(3)
sum = n1 + n2
print("sum=", sum)
sub = n1 - n2
print("sub=", sub)
mul = n1 * n2
print("mul", mul)
div = n1 / n2
print("div", div)
floordiv = n1 // n2
print("floor div", floordiv)
p = n1 ** n2
print(f"(n1.num)raised to (n2.num)={p}")
