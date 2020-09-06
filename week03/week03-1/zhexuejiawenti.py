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
        self.leftn=num
        self.rightn=num -1 if num >= 1 else dphnums -1

    def __call__(self):
        print(f'{self.number} start at {datetime.now().microsecond}')
        while self.eatn > 0:
            with l[self.leftn]:
                print(f'[{self.number},{self.leftn},2]')
                if not l[self.rightn].locked():                       
                    with l[self.rightn]:
                        print(f'[{self.number},{self.rightn},2]')
                        print(state)
                        sleep(1)
                        q.put(self.number)
            state[self.number]=0
            self.eatn -= 1


if __name__ == '__main__':
    dphnums=5
    q=queue.Queue(5)
    #print(q.qsize())
    #state=[0]*5
    l=[]
    for i in range(5):
        l.append(Lock())
    #pool = ThreadPoolExecutor(5)
    t=[]
    #print('init task')
    for i in range(5):
        t.append(threading.Thread(target=DiningPhilosophers(i,4,l)))
    #print('start task')
    for i in range(5):
        t[i].start()
    for i in range(5):
        t[i].join()
