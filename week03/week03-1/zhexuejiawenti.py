#!/usr/local/bin/python3
#coding: utf-8

import threading
from threading import Lock
import queue
from concurrent.futures import ThreadPoolExecutor
from time import ctime,sleep
from datetime import datetime


class  DiningPhilosophers:
    def __init__(self,num,eatn,l):
        #print(q.qsize())
        self.l=l
        self.eatn=eatn
        self.number=num  #0-4
        self.leftn=num   #0-4
        self.rightn=num -1 if num >= 1 else dphnums -1  #3,2

    def __call__(self):
        print(f'{self.number} started at {datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S.%f")}')
        while self.eatn > 0:
            with l[self.leftn]:
                #print(f'[{self.number},{self.leftn},2]')
                if not l[self.rightn].locked():                       
                    with l[self.rightn]:
                        print(f'{self.number} is eating at {datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S.%f")}')
                        print(f'[{self.number},{self.leftn},2]')
                        print(f'[{self.number},{self.rightn},2]')
                        sleep(1)
                        print(f'{self.number} is done at {datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S.%f")}')
                        self.eatn -= 1
            #print(f'{self.number},{self.eatn}')
            
            


if __name__ == '__main__':
    dphnums=5
    #q=queue.Queue(5)
    #print(q.qsize())
    #state=[0]*5
    #pool = ThreadPoolExecutor(5)
    l=[]
    for i in range(5):
        l.append(Lock())

    t=[]
    for i in range(5):
        t.append(threading.Thread(target=DiningPhilosophers(i,4,l)))
    for i in range(5):
        t[i].start()
    for i in range(5):
        t[i].join()
