from threading import Thread
class sumThread(Thread):
    sum = 0
    n= 5

    def run(self):
        for i in range(1, self.n + 1):
            self.sum = self.sum + i
            print(f"sum of 1 to {i}={self.sum}")
class factThread(Thread):
    fact=1
    n=5
    def run(self):
        for i in range(1,self.n+1):
            self.fact=self.fact*i
            print(f"factorial of 1 to {i}={self.fact}")


st = sumThread()
ft = factThread()
st.setName("sumThread")
ft.setName("factThread")
print(f"is {st.getName()}started={st.is_alive()}")
print(f"is {ft.getName()}started={ft.is_alive()}")
st.start()
ft.start()
