'''
    read_directory 
    input: file_path，帧集合，这里一次只能处理一个视频的帧集合，因此迭代要放在main或其他上一级程序中
    ，xy_path 注视位置，即load_asc中的v3所在位置，建议在一个文件夹中保存，和原始以及v2区分开来，
    save_path， 区域灰度强度及其他数据保存位置，含文件名
'''

import os
import numpy
import cv2
import pandas as pd
import matplotlib.pyplot as plt

def read_directory(file_path,xy_path,save_path):
    framefile = pd.read_csv(xy_path,skiprows=1)
    x=framefile.iloc[:,0]
    x=numpy.array(x.values.tolist())
    y=framefile.iloc[:,1]
    y=numpy.array(y.values.tolist())
    number_pic=len([name for name in os.listdir(file_path) if os.path.isfile(os.path.join(file_path, name))])
    if len(x)<number_pic:
    # 在数组前添加缺少的成员（-1），取整个图片灰度强度，用作眼动延迟
        data_x=numpy.zeros((number_pic-len(x),), dtype = float, order = 'C')
        data_y=numpy.zeros((number_pic-len(x),), dtype = float, order = 'C')
        data_x=numpy.hstack((data_x,x))
        data_y=numpy.hstack((data_y,y))

    img_gray_all=[]
    img_gray_part=[]
    for i,file_name in enumerate(os.listdir(file_path)):
        img=cv2.imread(file_path+'/'+file_name)
        img_gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        # img_gray是[360,540]的二维数组，取中心点然后截取矩形即可，这里试验可以用随机二维
        y=int(round(data_x[i]/3))
        x=int(round(data_y[i]/3))
        '''
        if(x-10>0)and(x+10<360)and(y-10>0)and(y+10<640):
        # x长，y宽，眼动数据记录里是(宽，长)，cv读取的数组是（长，宽）
            img_gray_part.append(numpy.nanmean(img_gray[x-10:x+10,y-10:y+10]))
        else:
            img_gray_part.append(numpy.nanmean(img_gray))
        '''
        if(x-10>0)and(x+10<360)and(y-10>0)and(y+10<640):
            img_gray_part.append(numpy.nanmean(img_gray[x-10:x+10,y-10:y+10]))
        else:
            img_gray_part.append(-1)

        img_gray_all.append(numpy.nanmean(img_gray))
    numpy.savetxt(save_path,img_gray_part,fmt='%f',delimiter = ',',header='img_gray_part',comments='')

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



