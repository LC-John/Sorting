#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 18 14:48:03 2018

@author: zhanghuangzhao
"""

import numpy
import copy
import os, shutil

import imageio
import matplotlib.pyplot as plt

size = 20
arr = None

def BubbleSort(a, reverse=False):
    
    a = copy.deepcopy(a)
    l = len(a)
    proc = []
    
    proc.append(copy.deepcopy(a))
    for i in range(l):
        for j in range(i+1, l):
            if (reverse and a[i] > a[j]) \
                or ((not reverse) and a[i] < a[j]):
                    (a[i], a[j]) = (a[j], a[i])
            proc.append(copy.deepcopy(a))
    
    return a, proc

if __name__ == "__main__":
    
    arr = numpy.random.uniform(0, 1, size=size)
    arr = arr.tolist()
    
    res, proc = BubbleSort(arr)
    
    tmp_dir = "../images/tmp"
    img_buf = []
    if os.path.isdir(tmp_dir):
        shutil.rmtree(tmp_dir)
    os.mkdir(tmp_dir)
    for i in range(len(proc)):
        plt.cla()
        plt.bar(x=list(range(size)),
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
    imageio.mimsave("../images/BubbleSort.gif", img_buf)