#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 23 13:55:02 2018

@author: zhanghuangzhao
"""

import numpy

import copy
import os, shutil

import imageio
import matplotlib.pyplot as plt

size = 8
arr = None
    
def SlowSort(a, idx_begin, idx_end, reverse=False):
    
    a = copy.deepcopy(a)
    proc = []
    
    if idx_begin >= idx_end:
        return a, proc
    
    idx_mid = int(numpy.floor((idx_begin+idx_end)/2))
    a, tmp_proc = SlowSort(a, idx_begin, idx_mid, reverse)
    proc += tmp_proc
    a, tmp_proc = SlowSort(a, idx_mid+1, idx_end, reverse)
    proc += tmp_proc
    
    if (reverse and a[idx_mid] > a[idx_end]) \
        or ((not reverse) and a[idx_mid] < a[idx_end]):
        (a[idx_mid], a[idx_end]) = (a[idx_end], a[idx_mid])
    proc.append(copy.deepcopy(a))
    
    a, tmp_proc = SlowSort(a, idx_begin, idx_end-1, reverse)
    proc += tmp_proc
        
    return a, proc

if __name__ == "__main__":
    
    arr = numpy.random.uniform(0, 1, size=size)
    arr = arr.tolist()
    
    res, proc = SlowSort(arr, 0, len(arr)-1)
    
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
    imageio.mimsave("../images/SlowSort.gif", img_buf)