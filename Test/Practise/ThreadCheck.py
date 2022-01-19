import time
from threading import Thread


class sag(Thread):
    def run(self):
        for i in range(40):
          print("Hi sag")
          time.sleep(1)

class sa(Thread):
    def run(self):
        for i in range(8):
         print("hi")

         time.sleep(1)


t1=sag()
t2=sa()

t1.start()
time.sleep(1)

t2.start()
time.sleep(1)