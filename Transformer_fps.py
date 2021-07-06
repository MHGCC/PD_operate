from moviepy.editor import *
video_input_path='D:/Search/project01/data/tvsum50_ver_1_1/ydata-tvsum50-v1_1/ydata-tvsum50-video/video_43.mp4'
video_output_path='D:/Search/project01/data/tvsum50_ver_1_1/ydata-tvsum50-v1_1/ydata-tvsum50-video/video_43_v2.mp4'
clip = VideoFileClip(video_input_path)
clip.write_videofile(video_output_path, fps=50)