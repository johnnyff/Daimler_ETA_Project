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
import sys

if __name__ == '__main__':
    df = pd.DataFrame(columns=['vehicleCode', 'lat', 'lng', 'timestamp', 'distance', 'is_in_target', \
                               'del_time', 'velocity', 'weekday', 'journey' \
                                                                  'velocity_mean_sec', 'velocity_std_sec', \
                               'velocity_mean_day', 'velocity_std_day', 'cum_sum', 'total_distance', \
                               'left_distance', 'time_cum_sum', 'total_time', 'now_state'])


    truck_instance = Truck(df)
    truck_instance.set_initial_timestamp(sys.argv[6])


    #while
    input_data = sys.argv
    print("input data", input_data)

    df.loc[0,'lat'] = sys.argv[1]
    df.loc[0,'lng'] = sys.argv[2]
    df.loc[0,'distance'] = float(sys.argv[3])
    df.loc[0,'vehicleCode'] = sys.argv[4]
    df.loc[0,'journey'] = sys.argv[5]
    df.loc[0,'timestamp'] = sys.argv[6]

    df = set_constant_info(df,sys.argv[4])
    df = update(truck_instance)
    for i in df.columns:
        print(i, " : ", df.loc[0,i])
    ##predict_model()