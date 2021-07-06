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

    x=numpy.arange(1,len(img_gray_all)+1)
    plt.figure()
    l1=plt.plot(x,img_gray_all,'r--',label='all')    
    plt.xlabel('Frame')
    plt.ylabel('Gray intensity')
    plt.figure()
    l2=plt.plot(x,img_gray_part,'g-.',label='part')
    plt.xlabel('Frame')
    plt.ylabel('Gray intensity')

    plt.legend()
    plt.show()
    
    #numpy.savetxt(save_path,img_gray_part,fmt='%f',delimiter = ',',header='img_gray_part',comments='')

        
    return 



def main():

    array_of_img=[]
    file_path='D:/Project/PD_operate/data/video_43/'
    xy_path='D:/Project/PD_operate/data/1_video_43_v3.csv'
    save_path='D:/Project/PD_operate/data/1_video_43_gray_intensity.csv'
    array_of_img=read_directory(file_path,xy_path,save_path)


if __name__=='__main__':
    main()