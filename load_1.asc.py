import os 
import numpy as np
import re

def read_file(file_path):
    count=0
    i=0
    flag_start=False
    flag_end=False
    data_id=[]
    data_x=[]
    data_y=[]
    data_pupilD=[]

    with open(file_path,'r') as F:
        for line in F:
            flag_1=re.search('TRIALSTART',line)
            flag_2=re.search('TRIALEND',line)
            # 这里要建立控制逻辑，flag_1不为None，设置flag_start为真，启动记录，flag_2不为None
            # flag_start为False，记录关闭，同时记录video_No
            if(flag_1!=None):
                flag_start=True
                x=re.search('stimuli',line)
                video_name=line[x.span()[1]+1:-1]
                pass
                pass
            if(flag_2!=None):
                flag_start=False
                count=count+1
                data_id=np.array(data_id)
                data_x=np.array(data_x)
                data_y=np.array(data_y)
                data_pupilD=np.array(data_pupilD)
                np.savetxt('D:/Project/PD_operate/data/'+str(count)+'_'+video_name+'.csv'
                ,np.column_stack((data_id,data_x,data_y,data_pupilD)),fmt='%s',delimiter = ',',header='id,x,y,pupilD',comments='')
                i=0
                data_id=[]
                data_x=[]
                data_y=[]
                data_pupilD=[]
            if(flag_start):
                # 确认在start,end范围内，排除掉EFIX、ESACC之类的影响，其共性是line起始位置不是
                # 数值0-9
                # 复杂一点可以再分清楚FIX、SACC以及BLINK
                flag_3=line[0]
                if flag_3.isdigit():
                    # 这里还要再保存为str，所以不用类型转换
                    eye_data=line.split()
                    id=eye_data[0][:]
                    data_id.append(eye_data[0][:])
                    if eye_data[0][:]=='3828558':
                        print('here')
                    x=eye_data[1][:]
                    data_x.append(eye_data[1][:])
                    y=eye_data[2][:]
                    data_y.append(eye_data[2][:])
                    pupilD=eye_data[3][:]
                    data_pupilD.append(eye_data[3][:])
                    i=i+1

def main():
    file_path='D:/Project/PD_operate/data/1.asc'
    read_file(file_path)

main()

