# -*- coding: utf-8 -*-
"""
Created on Wed Dec 19 09:04:37 2018

@author: DrLC
"""

import numpy
import random

import copy
import os, shutil

import imageio
import matplotlib.pyplot as plt

size = 8
arr = None

def Sorted(a, reverse=False):
    
    a = copy.deepcopy(a)
    l = len(a)
    
    for i in range(1, l):
        if (reverse and a[i-1] > a[i]) \
            or ((not reverse) and a[i-1] < a[i]):
            return False
    return True
            
def BogoSort(a, reverse=False):
    
    a = copy.deepcopy(a)
    l = len(a)
    proc = []
    
    proc.append(copy.deepcopy(a))
    while not Sorted(a, reverse):
        a = random.sample(a, l)
        proc.append(copy.deepcopy(a))
    
    return a, proc

if __name__ == "__main__":
    
    arr = numpy.random.uniform(0, 1, size=size)
    arr = arr.tolist()
    
    res, proc = BogoSort(arr)
    
    tmp_dir = "../images/tmp"
    img_buf = []
    if os.path.isdir(tmp_dir):
        shutil.rmtree(tmp_dir)
    os.mkdir(tmp_dir)
    for i in range(len(proc)):
        plt.cla()
        plt.bar(list(range(size)),
                height=proc[i],
                width=0.5)
        plt.savefig(os.path.join(tmp_dir, ("%d.jpg" % i)))
        img_buf.append(imageio.imread(os.path.join(tmp_dir, ("%d.jpg" % i))))
        print ("\r%d / %d" % (i+1, len(proc)), end="")
    print("\ndone!")
    plt.cla()
    init = [imageio.imread(os.path.join(tmp_dir, "0.jpg")) for i in range(10)]
    final = [imageio.imread(os.path.join(tmp_dir, ("%d.jpg" % (len(proc)-1)))) for i in range(10)]
    img_buf = init + img_buf + final
    shutil.rmtree(tmp_dir)
    imageio.mimsave("../images/BogoSort.gif", img_buf)