import numpy as np
import pandas as pd
import math

def data_cut(raw_data):

    arr_mean=np.mean(raw_data)
    arr_std=np.std(raw_data,ddof=1)
    new_data=np.empty([len(raw_data)],dtype=int)
    for i in range(0,len(raw_data)):
        new_data[i]=math.floor(int((raw_data[i]-arr_mean)/arr_std))
    
    return new_data,arr_mean,arr_std

def main():
    raw_data=[1,2,3,4,5]
    new_data,arr_mean,arr_std=data_cut(raw_data)
    print('arr_mean={}, arr_std={}'.format(arr_mean,arr_std))
    print(new_data)

if __name__=='__main__':
    main()


