import os
import numpy
import cv2
import pandas as pd
import matplotlib.pyplot as plt

def plot(data,save_path,model,label=None,title=None,axis_x=None,axis_y=None):
    # 传入numpy数组data，剩下的是图上的组件
    # 确实，这样的话就不能或者很难画，得加个模式，model，1,2,3表示同时画几条线，data作二维数组


    plt.figure()
    if model==1:
        x=numpy.arange(1,data.shape[0]+1)
        if label!=None:
            l1=plt.plot(x,data,'r--',label=label)
        else:
            l1=plt.plot(x,data,'r--')


    elif model==2:
        x=numpy.arange(1,data.shape[1]+1)
        if label!=None:
            l1=plt.plot(x,data[0,:],'r--',label=label[0])
            l2=plt.plot(x,data[1,:],'g.-',label=label[1])
        else:
            l1=plt.plot(x,data[0,:],'r--')
            l2=plt.plot(x,data[1,:],'g.-')

    else:
        x=numpy.arange(1,data.shape[1]+1)
        if label!=None:
            l1=plt.plot(x,data[0,:],'r--',label=label[0])
            l2=plt.plot(x,data[1,:],'r.-',label=label[1])
            l3=plt.plot(x,data[2,:],'b*-',label=label[2])
        else:
            l1=plt.plot(x,data,'r--')
    
    if axis_x!=None and axis_y!=None:
        plt.xlabel(axis_x)
        plt.ylabel(axis_y)
        plt.legend()
    if title!=None:
        plt.title(title)    
    # save必须在show之前，因为show会创建空画板
    plt.savefig(save_path)
    plt.show()
    plt.close()



