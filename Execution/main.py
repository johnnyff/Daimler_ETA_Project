import datetime
import pandas as pd
import time
import sys
import pickle

from Truck import Truck
from util import update, set_constant_info, set_initial_info
from inference import predict_model


if __name__ == '__main__':
    ("main task started")
    df = pd.DataFrame(columns=['vehicleCode', 'lat', 'lng', 'timestamp', 'distance', 'is_in_target', \
                               'del_time', 'velocity', 'weekday', 'journey','velocity_mean_5sec', 'velocity_std_5sec', \
                               'velocity_mean_day', 'velocity_std_day', 'cum_sum', 'avg_total_distance', \
                               'left_distance', 'time_cum_sum', 'avg_total_time', 'now_state'])

    #get initial input value : vehicleCode & Journey info
    initial_input = sys.argv[1:]
    vehicleCode= initial_input[0]
    journey = initial_input[1]

    #prior knowledge data load
    avg_route_info = pd.read_csv("./data/constant_total_distance_time.csv", encoding='shift_jis')
    velocity_5sec_info = pd.read_csv("./data/constant_velocity_5sec.csv", encoding='shift_jis')
    velocity_weekday_info = pd.read_csv("./data/constant_velocity_weekday.csv", encoding='shift_jis')

    #model_load
    model = pickle.load(open("./model/final_model_insight.model", 'rb'))
    df = set_initial_info(df, avg_route_info, vehicleCode, journey)

    #make truck instance
    truck_instance = Truck(df, velocity_5sec_info, velocity_weekday_info)

    print("setting is done! ETA process started!")
    print("-------------------------------------")
    # every each time timestamp comes in, the values are updated automatically and return left time
    while(True):

        #get gpsdata (lat,lng, distance, timestamp)
        #later we can transfer data by another source
        input_data = input()
        if(input_data =='q'):
            break

        argv = input_data.split()

        #execution will be done only once(the first day)
        truck_instance.set_initial_timestamp(argv[3])

        #update the instance's values
        #print("input data", input_data)
        df.loc[0,'lat'] = argv[0]
        df.loc[0,'lng'] = argv[1]
        df.loc[0,'distance'] = float(argv[2])
        df.loc[0,'timestamp'] = argv[3]


        df = update(truck_instance)

        if(truck_instance.df.loc[0,'left_distance']==0):
            print("Vehicle is Arrived! ")
            break
        ##for checking realtime input data status
        #for i in df.columns:
        #    print(i, " : ", df.loc[0,i])

        res = predict_model(df, model)
        print("left time : {} minutes".format(res))