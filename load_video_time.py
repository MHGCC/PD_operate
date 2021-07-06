'''
    这段代码用于获取一个文件夹下的视频的信息
    input:path
    output:video_feature，打包成numpy数组
    输出为到指定的txt文件中
'''

import cv2
import os

def load_video_feature(file_path):
    cap=cv2.VideoCapture(file_path)
    if cap.isOpened():
        rate=cap.get(5)
        frame_number=cap.get(7)
        duration=frame_number/rate/60

    return rate,frame_number,duration

def read_filepath(path):
    files=os.listdir(path)
    file_name={}
    rate={}
    frame_number={}
    duration={}

    for i,file in enumerate(files):
        if not os.path.isdir(file):
            file_name[i]=file
            file_path=path+'/'+file_name[i]
            rate[i],frame_number[i],duration[i]=load_video_feature(file_path)
        
    return file_name,rate,frame_number,duration

def main():

    path='D:/Project/video_ding/video_ding_1/movie1'
    file_name,rate,frame_number,duration=read_filepath(path)
    with open('D:/Project/PD_operate/data/test_data.txt','ab') as data:
        for i in range(0,len(rate)):
            data.write('file_name:{}, rate:{}, frame_number:{}, duration:{}'.format(file_name[i],rate[i],frame_number[i],duration[i]).encode())
            data.write('\n'.encode())   #这样搞，换行被无效了

if __name__=='__main__':
    main()

