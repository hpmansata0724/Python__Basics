from pprint import pp
from threading import Thread, Lock
import time


class myThread(Thread):
    def __init__(self, Threadid, name, delay):
        Thread.__init__(self)
        self.Threadid = Threadid
        self.name = name
        self.delay = delay

    def pp(name, delay, counter):
        while counter:
            time.sleep(delay)
            print(f"{name}:{time.ctime(time.time())}")
            counter -= 1

    # def pp(Threadname, delay, counter):
    # while counter:
    #     time.sleep(delay)
    #     print(f"{Threadname}:{time.ctime()}")
    #     counter -= 1

    def run(self):
        print("starting" + self.name)
        ThreadLock.acquire()
        # pp(self.name, self.delay, 3)
        pp(self.name, self.delay, 3)
        Thread.Lock.release()


ThreadLock = Lock()
Threads = []
Thread1 = myThread(101, "Thread-1", 1)
Thread2 = myThread(102, "Thread-2", 2)
Thread1.start()
Thread2.start()
Threads.append(Thread1)
Threads.append(Thread2)
for t in Threads:
    t.join()
print("Exiting main Thread")