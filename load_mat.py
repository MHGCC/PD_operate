'''
这是读取v7.3后的mat文件，然后读取其中的内容的程序
遇到读取的np.array是ascaii数字而需要字符串的情况，转换即可

yu博士提供的文件似乎是v7.3前的mat文件，换方法
'''
import os
os.chdir(os.path.dirname(__file__))
import scipy.io as scio
import h5py
import numpy as np
import matplotlib.pyplot as plt
from my_normalization import normalization
from data_cut import data_cut
from move_average import move_average

'''
def smooth(a,WSZ):
    # a:原始数据，NumPy 1-D array containing the data to be smoothed
    # 必须是1-D的，如果不是，请使用 np.ravel()或者np.squeeze()转化 
    # WSZ: smoothing window size needs, which must be odd number,
    # as in the original MATLAB implementation
    out0 = np.convolve(a,np.ones(WSZ,dtype=int),'valid')/WSZ
    r = np.arange(1,WSZ-1,2)
    start = np.cumsum(a[:WSZ-1])[::2]/r
    stop = (np.cumsum(a[:-WSZ:-1])[::2]/r)[::-1]
    return np.concatenate((start,out0,stop))
'''

# arr已经是numpy.arr了，可以正常操作
data_pupilD={}
smooth_data_pupilD={}
cut_data_pupilD={}

for mov_i in range(1,13):
    data_path='D:/Project/PD_operate/data/video1_pupilD/mov-{}.mat'.format(mov_i)
    data_mat=scio.loadmat(data_path)
    data_pupilD[mov_i]=data_mat['data']
    #y=normalization(data_pupilD[mov_i].squeeze())
    y=data_pupilD[mov_i].squeeze()
    y=move_average(y,8)
    smooth_data_pupilD[mov_i]=y
    y,arr_mean,arr_std=data_cut(y)
    cut_data_pupilD[mov_i]=y
    
    # 可以把plot独立函数
    x=np.arange(1,len(data_pupilD[mov_i])+1)
    plt.figure()
    #l1=plt.plot(x,data_pupilD[mov_i],'r--',label='row')
    #l2=plt.plot(x,smooth_data_pupilD[mov_i],'g--',label='smooth')
    l1=plt.plot(x,data_pupilD[mov_i],'r--',label='raw')
    l2=plt.plot(x,smooth_data_pupilD[mov_i],'g-.',label='smooth')
    #plt.legend()
    plt.twinx()
    #l3=plt.plot(x,cut_data_pupilD[mov_i],'b--',label='cut')
    l3=plt.plot(x,cut_data_pupilD[mov_i],'b-',label='cut')
    plt.title('mov-{} pupilD'.format(mov_i))
    plt.xlabel('time')
    plt.ylabel('pupilD')
    lns=l1+l2+l3
    labs=[l.get_label() for l in lns]
    plt.legend(lns,labs,loc='best')
    '''
        碰到这种双坐标中，在plot中标legend会重叠，设置合并图例
    '''
    plt.savefig('D:/Search/project01/data/log/6.15-6.18/pictures/mov-{}.tiff'.format(mov_i))
    # plt.show()


