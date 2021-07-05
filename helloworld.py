import pandas as pd
import numpy as np
from tools.plots_and_others import plot


a=[1,2,3]
b=[[1,2,3],[4,5,6],[7,8,9]]

a=np.array(a)
b=np.array(b)

plot(a,save_path='D:/Project/PD_operate/data/a.tiff',model=1)
plot(b,save_path='D:/Project/PD_operate/data/b.tiff',model=3,label=['111','222','333'],axis_x='x',axis_y='y',title='x-y')