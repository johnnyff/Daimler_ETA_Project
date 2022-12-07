import random
import datetime
import pandas as pd
import numpy as np
from datetime import datetime
import time
from tqdm import tqdm
import gc
from Truck import Truck
from util import update, set_constant_info
from inference import predict_model
import sys
import pickle

if __name__ == '__main__':
    ("main task started")
    df = pd.DataFrame(columns=['vehicleCode', 'lat', 'lng', 'timestamp', 'distance', 'is_in_target', \
                               'del_time', 'velocity', 'weekday', 'journey' \
                                                                  'velocity_mean_sec', 'velocity_std_sec', \
                               'velocity_mean_day', 'velocity_std_day', 'cum_sum', 'total_distance', \
                               'left_distance', 'time_cum_sum', 'total_time', 'now_state'])


    truck_instance = Truck(df)


    #model = pickle.load(open('model.pkl', 'rb'))

    while(True):
        input_data = input()
        if(input_data =='q'):
            break
        argv = input_data.split()
        truck_instance.set_initial_timestamp(argv[5])

        print("input data", input_data)

        df.loc[0,'lat'] = argv[0]
        df.loc[0,'lng'] = argv[1]
        df.loc[0,'distance'] = float(argv[2])
        df.loc[0,'vehicleCode'] = argv[3]
        df.loc[0,'journey'] = argv[4]
        df.loc[0,'timestamp'] = argv[5]

        df = set_constant_info(df,argv[3])
        df = update(truck_instance)
        for i in df.columns:
            print(i, " : ", df.loc[0,i])
        #res = predict_model(df)
        #print("res : ", res)