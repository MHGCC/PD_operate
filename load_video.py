import os
import sys
from moviepy.editor import VideoFileClip
import argparse
import numpy as np
import cv2

def video_transformer(video_path,new_video_path,fps):
    clip = VideoFileClip(video_path)
    clip.write_videofile(new_video_path, fps=fps)

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
            # 用来降低帧率，一般用不到
        dig=str(frame_count)
        dig=dig.zfill(6)
        path=save_path+'/'+str(dig)+'.jpg'
        cv2.imwrite(path,frame)
        
        success,frame=cap.read()
    
    cap.release()
    return

def main():
    video_path='D:/Search/project01/data/tvsum50_ver_1_1/ydata-tvsum50-v1_1/ydata-tvsum50-video/video_11.mp4'
    new_video_path='D:/Project//data_try/video_11_fps=25.mp4'
    frame_save_path='D:/Project/data_try/video_11'
    fps=25
    video_transformer(video_path,new_video_path,fps=fps)
    get_video(new_video_path,frame_save_path)

if __name__=='__main__':
    main()




