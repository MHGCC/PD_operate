import pandas as pd
import numpy as np

def read_asc(file_path,save_path):
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
        
        if int(framefile.iloc[i,0])==3846452:
            print('here')
        # 测试眨眼区，在文件中是以符号'.'为标记
        
        x=framefile.iloc[i,1]
        if framefile.iloc[i,1]!='.':
            data_x.append(float(framefile.iloc[i,1]))
            data_y.append(float(framefile.iloc[i,2]))
            data_pupilD.append(float(framefile.iloc[i,3]))
        else:
            data_x.append(data_x[i-1])
            data_y.append(data_y[i-1])
            data_pupilD.append(data_pupilD[i-1])
        # 通过这一步填充眨眼区
    np.savetxt(save_path
                ,np.column_stack((data_id,data_x,data_y,data_pupilD)),fmt='%s',delimiter = ',',header='id,x,y,pupilD',comments='')
    
    data_x_mean=[]
    data_y_mean=[]
    data_pupilD_mean=[]
    for i in range(0,round(framefile.shape[0]/)):
        if i!=round(framefile.shape[0]/10)-1:
            data_x_mean.append(np.mean(data_x[i*10:(i+1)*10]))
            data_y_mean.append(np.mean(data_y[i*10:(i+1)*10]))
            data_pupilD_mean.append(np.mean(data_pupilD[i*10:(i+1)*10]))
        else:
            data_x_mean.append(np.mean(data_x[i*10:]))
            data_y_mean.append(np.mean(data_y[i*10:]))
            data_pupilD_mean.append(np.mean(data_pupilD[i*10:]))

    save_path='D:/Project/PD_operate/data/1_video_43_v3.csv'
    np.savetxt(save_path
                ,np.column_stack((data_x_mean,data_y_mean,data_pupilD_mean)),fmt='%s',delimiter = ',',header='x,y,pupilD',comments='')

    return 



def main():
    file_path='D:/Project/PD_operate/data/1_video_43.avi.csv'
    save_path='D:/Project/PD_operate/data/1_video_43_v2.csv'
    read_asc(file_path,save_path)

if __name__=='__main__':
    main()
