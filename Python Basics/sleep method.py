from threading import Thread
from time import sleep
class sumthread(Thread):
    sum=0
    n=5
    def run (self):
        for i in range(1,self.n+1):
            if i%2==0:
                print(f"{self.getname()} is sleeping mode for 2sec" )
                sleep(2)
            self.sum=self.sum+i
            print(f"sem of 1 to {i}={self.sum}")
class factThread:
    fact=1
    n=5
    def run(self):
        for i in range(1,self.n+1):
            if i%3==0:
                print(f"{self.getname()} is sleeping mode for 2sec")
                sleep(2)

            self.fact=self.fact*i
            print(f"factorial of 1 to {i}={self.fact}")
st=sumthread()
ft=factThread()
st.setname("sumThread")
ft.setname("factThread")
print(f"is{st.getname()}started={st.is_alive()}")
print(f"is{ft.getname()}started={ft.is_alive()}")
st.start()
ft.start()


