import os
from tools.load_asc import *

def main():

    asc_file_path='D:/Project/PD_operate/data/1.asc'
    csv_save_path='D:/Project/data_try'
    read_file(asc_file_path,csv_save_path)
    # 这一步之后已在csv_save_path生成了n个切割好的csv文件，进行迭代
    for i,file_name in enumerate(os.listdir(csv_save_path)):
        csv_file=csv_save_path+'/'+file_name
        csv_file_save_path=csv_save_path+'/'+file_name
        read_asc(csv_file,csv_file_save_path,time=20)

main()