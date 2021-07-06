import os
import sys
from moviepy.editor import VideoFileClip
import argparse
import numpy as np
import cv2

'''
class FileCheck():

    def get_filesize(self, filename): # 获取文件大小
        file_byte = os.path.getsize(filename)
        return self.sizeConvert(file_byte)

    def get_file_times(self, filename): # 获取文件时长
        clip = VideoFileClip(filename)
        file_time = self.timeConvert(clip.duration)
        return file_time

    def sizeConvert(self, size):  # 文件大小单位换算
        K, M, G = 1024, 1024 ** 2, 1024 ** 3
        if size >= G:
            return str(round((size / G), 2)) + ' G Bytes'

        elif size >= M:
            return str(round((size / M), 2)) + ' M Bytes'

        elif size >= K:
            return str(round((size / K), 2)) + ' K Bytes'

        else:
            return str(round((size), 3)) + ' Bytes'

    def timeConvert(self, size):  # 文件时长单位换算
        M, H = 60, 60 ** 2
        if size < M:
            return str(size) + u'秒'
        if size < H:
            return u'%s 分 %s 秒 ' % (int(size / M), int(size % M))
        else:
            hour = int(size / H)
            mine = int(size % H / M)
            second = int(size % H % M)
            tim_srt = u'%s 小时 %s 分 %s 秒 ' % (hour, mine, second)
            return tim_srt

    def get_file(self): # 从命令行获取文件名
        fname = args.fname
        return fname
'''

def get_video(video_path,save_path,gaze_x=None,gaze_y=None):
    cap=cv2.VideoCapture(video_path)
    fps=cap.get(cv2.CAP_PROP_FPS)
    total=int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    width=cap.get(cv2.CAP_PROP_FRAME_WIDTH)
    height=cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
    print('video_path: ',video_path)
    print('fps: ',fps)
    print('total_frames: ',total)
    print('video_time: ',total/fps)
    print('width: ',width)
    print('height: ',height)

    success,frame=cap.read()
    frame_count=0

    while success:
        frame_count=frame_count+1
        #if frame_count % int(fps)==0:
            # 提取注视点附近的灰度强度
        dig=str(frame_count)
        dig=dig.zfill(6)
        path=save_path+'/'+str(dig)+'.jpg'
        cv2.imwrite(path,frame)
        
        success,frame=cap.read()
    
    cap.release()
    return

def main():
    video_path='D:/Search/project01/data/tvsum50_ver_1_1/ydata-tvsum50-v1_1/ydata-tvsum50-video/video_43_v2.mp4'
    save_path='D:/Project/PD_operate/data/video_43/'
    get_video(video_path,save_path)

if __name__=='__main__':
    main()




