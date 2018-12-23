# -*- coding: utf-8 -*-
"""
Created on Wed Dec 19 09:41:20 2018

@author: DrLC
"""

import numpy
import time
import threading

import copy
import os, shutil

import imageio
import matplotlib.pyplot as plt

size = 8
arr = None

img_buf = []

def Sleep(num):
    
    time.sleep(num)

class SleepThread (threading.Thread):
    
    def __init__(self, num, proc, res, reverse=False, maxval=1):
        
        threading.Thread.__init__(self)
        self.__num = num
        self.__res = res
        self.__proc = proc
        self.__reverse = reverse
        self.__maxval = maxval
        
    def run(self):
        
        if self.__reverse:
            Sleep(self.__num)
        else:
            Sleep(self.__maxval-self.__num)
        self.__res.append(self.__num)
        self.__proc.append(copy.deepcopy(self.__res))
    
def SleepSort(a, reverse=False, maxval=1):
    
    a = copy.deepcopy(a)
    l = len(a)
    res = []
    threads = []
    proc = []
    
    proc.append(copy.deepcopy(a))
    for i in range(l):
        threads.append(SleepThread(maxval-a[i], proc, res, reverse, maxval))
    for i in range(l):
        threads[i].start()
    for i in range(l):
        threads[i].join()
        
    return res, proc

if __name__ == "__main__":
    
    arr = numpy.random.uniform(0, 1, size=size)
    arr = arr.tolist()
    
    res, proc = SleepSort(arr)
    
    tmp_dir = "../images/tmp"
    img_buf = []
    if os.path.isdir(tmp_dir):
        shutil.rmtree(tmp_dir)
    os.mkdir(tmp_dir)
    for i in range(len(proc)):
        plt.cla()
        plt.bar(list(range(len(proc[i]))),
                height=proc[i],
                width=0.5)
        plt.xlim([-1, len(arr)])
        plt.ylim([-0.01, 1.01])
        plt.savefig(os.path.join(tmp_dir, ("%d.jpg" % i)))
        img_buf.append(imageio.imread(os.path.join(tmp_dir, ("%d.jpg" % i))))
        print ("\r%d / %d" % (i+1, len(proc)), end="")
    print("\ndone!")
    plt.cla()
    init = [imageio.imread(os.path.join(tmp_dir, "0.jpg")) for i in range(10)]
    final = [imageio.imread(os.path.join(tmp_dir, ("%d.jpg" % (len(proc)-1)))) for i in range(10)]
    img_buf = init + img_buf + final
    shutil.rmtree(tmp_dir)
    imageio.mimsave("../images/SleepSort.gif", img_buf)