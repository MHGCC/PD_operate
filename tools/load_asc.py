'''
    read_asc
    这里读取asc文件拆分成的.csv，如果要做成合适的tools
    input:file_path, save_path, save_path+'_v3.csv'是要提供给下一段处理程序读取需要的数据位置，v2用于存储, time, 提供一个用于fps匹配的值(默认眼动数据帧率高于原视频)
'''

'''
    read_file
    读取 原始数据.asc文件，然后传递给load_asc进行处理
    在main()中调用时，input  file_path--.asc文件地址，包含.asc后缀，save_path--拆分的.csv文件保存地址，'/'
'''

import os
import re
import pandas as pd
import numpy as np

def my_mean(data):
    total=0
    count=0
    for i in range(len(data)):
        if data[i]!=-1.0:
            total=total+data[i]
            count=count+1
        else:
            pass

    if count>0:
        mean_data=total/count
    else:
        mean_data=-1.0
    return mean_data

def read_asc(file_path,save_path,time):
    framefile = pd.read_csv(file_path,skiprows=0)
    #framefile=framefile.values.tolist()
    #framefile.to_csv(save_path,index=False,sep=',')
    #print(framefile.size)
    #print(framefile.shape)
    #print(framefile.ndim)
    data_id=[]
    data_x=[]
    data_y=[]
    data_pupilD=[]
    flag=False

    for i in range(0,framefile.shape[0]):
        data_id.append(int(framefile.iloc[i,0]))
        
        '''
        if int(framefile.iloc[i,0])==3846452:
            print('here')
        # 测试眨眼区，在文件中是以符号'.'为标记
        '''
        
        x=framefile.iloc[i,1]
        if framefile.iloc[i,1]!='.':
            data_x.append(float(framefile.iloc[i,1]))
            data_y.append(float(framefile.iloc[i,2]))
            data_pupilD.append(float(framefile.iloc[i,3]))
        else:
            data_x.append(-1.0)
            data_y.append(-1.0)
            data_pupilD.append(-1.0)
        # 通过这一步填充眨眼区
    np.savetxt(save_path+'_v2.csv'
                ,np.column_stack((data_id,data_x,data_y,data_pupilD)),fmt='%s',delimiter = ',',header='id,x,y,pupilD',comments='')
    data_x_mean=[]
    data_y_mean=[]
    data_pupilD_mean=[]
    # 这一步需要对read_file中的眨眼置-1的位置进行处理，再写个函数好了
    for i in range(0,round(framefile.shape[0]/time)):
        if i!=round(framefile.shape[0]/time)-1:
            data_x_mean.append(my_mean(data_x[i*time:(i+1)*time]))
            data_y_mean.append(my_mean(data_y[i*time:(i+1)*time]))
            data_pupilD_mean.append(my_mean(data_pupilD[i*time:(i+1)*time]))
        else:
            data_x_mean.append(my_mean(data_x[i*time:]))
            data_y_mean.append(my_mean(data_y[i*time:]))
            data_pupilD_mean.append(my_mean(data_pupilD[i*time:]))

    np.savetxt(save_path+'_v3.csv'
                ,np.column_stack((data_x_mean,data_y_mean,data_pupilD_mean)),fmt='%s',delimiter = ',',header='x,y,pupilD',comments='')

    return 


def read_file(file_path,save_path):
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
                np.savetxt(save_path+'/'+str(count)+'_'+video_name+'.csv'
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
                    '''
                    if eye_data[0][:]=='3828558':
                        print('here')
                    '''
                    x=eye_data[1][:]
                    data_x.append(eye_data[1][:])
                    y=eye_data[2][:]
                    data_y.append(eye_data[2][:])
                    pupilD=eye_data[3][:]
                    data_pupilD.append(eye_data[3][:])
                    i=i+1
    
    return



def main():
    '''
    file_path='D:/Project/PD_operate/data/2_video_19.avi.csv'
    save_path='D:/Project/PD_operate/data/2_video_19'
    read_asc(file_path,save_path,time=10)
    '''
    print('ok')

if __name__=='__main__':
    main()
