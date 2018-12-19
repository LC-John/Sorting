# -*- coding: utf-8 -*-
"""
Created on Wed Dec 19 10:28:40 2018

@author: DrLC
"""

import numpy
import copy
import os, shutil

import imageio
import matplotlib.pyplot as plt

size = 8
arr = None

def StoogeSort(a, idx_begin, idx_end, reverse=False):
    
    a = copy.deepcopy(a)
    proc = []
    if (reverse and a[idx_begin] > a[idx_end-1]) \
        or ((not reverse) and a[idx_begin] < a[idx_end-1]):
        (a[idx_begin], a[idx_end-1]) = (a[idx_end-1], a[idx_begin])
    proc.append(copy.deepcopy(a))
    if idx_end - idx_begin >= 3:
        one_third = int((idx_end - idx_begin) / 3)
        two_third = one_third * 2 + idx_begin
        one_third = one_third + idx_begin
        a, tmp_proc = StoogeSort(a, idx_begin, two_third, reverse)
        proc += tmp_proc
        a, tmp_proc = StoogeSort(a, one_third, idx_end, reverse)
        proc += tmp_proc
        a, tmp_proc = StoogeSort(a, idx_begin, two_third, reverse)
        proc += tmp_proc
        
    return a, proc

if __name__ == "__main__":
    
    arr = numpy.random.uniform(0, 1, size=size)
    arr = arr.tolist()
    
    res, proc = StoogeSort(arr, 0, len(arr))
    
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
    imageio.mimsave("../images/StoogeSort.gif", img_buf)