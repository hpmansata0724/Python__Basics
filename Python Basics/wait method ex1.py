import logging
import threading
import time
logging.basicConfig(level=logging.DEBUG,


                    format='%(asctime)s(%(threadname)-2s)%(message)s',)
def consumer(cond):
    """wait for the condition and use the resource"""
    logging.debug('starting consumer thread')
    t=threading.currentThread()
    with cond:
        cond.wait()
        logging.debug("Resource is available to consumer")
        with cond:
            logging.debug('Making resource available')
            cond.notifyaAll()
def producer(cond):
    """set up the resource to be used by the consumer"""
    logging.debig("Starting producer thread")
    with cond:
        logging.debug('Making resource available')
        cond.notifyaAll()
condition=threading.Condition()
c1=threading.Thread(name='c1,target=consumer,args=(condition,)')
c2=threading.Thread(name='c2',target=consumer,args=(condition,))
p=threading.Thread(name='p',target=producer,args=(condition,))
c1.start()
time.sleep(2)
c2.start()
time.sleep(2)
p.start
