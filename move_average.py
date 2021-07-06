import numpy as np
import pandas as pd
import math

def move_average(data,wsz):
    #data取numpy数组类型
    s=pd.DataFrame(data)
    moving_avg = s.rolling(window=wsz,center=True).mean()
    # print(moving_avg)
    moving_avg=moving_avg.values
    moving_avg=moving_avg.squeeze()
    moving_avg[0:math.floor(wsz/2)]=data[0:math.floor(wsz/2)]
    moving_avg[-math.floor(wsz/2)+1:]=data[-math.floor(wsz/2)+1:]

    return moving_avg

def main():
    data=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19]
    data=np.asarray(data)
    moving_data=move_average(data,wsz=8)
    print(moving_data)

if __name__=='__main__':
    main()