from threading import Thread
import time
exitflag=0
def print_time(tname,counter,delay):
    while(counter):
        if exitflag:
            tname.exit()
        time.sleep(delay)
        print(f"{tname}={time.ctime(time.time())}")
        counter-=1
class myThread(Thread):
    def __init__(self,Threadld,Threadname,delay):
        Thread.__init__(self)
        self.Threadld=Threadld
        self.Threadname=Threadname
        self.delay=delay
    def run(self):
        print(f"string{self.Threadname}")
        print_time(self.Threadname,5,self.delay)
        print(f"exiting{self.Threadname}")
t1=myThread(101,"Thread-1",2)
t2=myThread(201,"Thread-2",3)
t1.start()
t2.start()

