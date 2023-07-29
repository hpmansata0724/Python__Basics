import time
import os
ticks=time.time()
print("Number of ticks since 12:00 am,January 1,1970:",1970)
print("Getting current Time->")
localtime=time.localtime(time.time())
print("local current time:",localtime)

print("Getting formatted time->")
localtime1=time.asctime(time.localtime(time.time()))
print("Local Currenttime:",localtime1)

print("time.sleep()Function->")
'''The method sleep() suspends execution for the given number of seconds. 
The arguement may be floating point number to indicate more precise sleep time. '''
print("Start: %s"%time.ctime())
time.sleep(5)
print("end : %s"%time.ctime())


