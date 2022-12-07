from haversine import haversine
import pandas as pd
import datetime
import yaml

def update(truck):
    truck.df = time_processing(truck.df)
    truck.df = update_isin_target(truck.df)
    truck = update_del_time(truck)
    truck.df = update_velocity(truck.df)
    truck.df = update_weekday(truck.df)
    truck = update_cumsum_distance(truck)
    truck = update_cumsum_time(truck)
    truck.update_now_state()
    truck = update_now_state(truck)
    return truck.df

def update_now_state(truck):
    idx = truck.get_state()
    idx_2 = (idx+1)%len(truck.df.loc[0,'journey'])
    label = str(idx)+str(idx_2)+truck.df.loc[0,'vehicleCode']
    truck.df.loc[0,'now_state']= label
    return truck
def set_constant_info(df,vehicle):
    with open('df_to_yaml.yaml', mode="rt", encoding="utf-8") as test_df_to_yaml:
        constant_df = pd.DataFrame(yaml.full_load(test_df_to_yaml)['result'])
    df.loc[0,'total_distance']=  constant_df[constant_df['vehicleCode']==vehicle]['mean_total_distance'][0]
    df.loc[0,'total_time']=  constant_df[constant_df['vehicleCode']==vehicle]['mean_total_time'][0]
    return df
def update_cumsum_time(truck):
    truck.cum_time += truck.df['del_time']
    truck.df['time_cum_sum'] = truck.cum_time
    return truck
def update_cumsum_distance(truck):
    truck.cum_distance += truck.df['distance']
    truck.df['cum_sum'] = truck.cum_distance
    return truck

def update_weekday(df):
    df['weekday'] = df['timestamp'].dt.weekday
    return df

def update_velocity(df):
    if(df.loc[0,'del_time']==0):
        df.loc[0,'velocity']=0
        return df
    df.loc[0,'velocity'] = df.loc[0,'distance']/df.loc[0,'del_time']
    return df

def update_del_time(truck):
    truck.df.loc[0,'del_time'] = (truck.df.loc[0,'timestamp'] - truck.prev_timestamp).seconds
    truck.prev_timestamp = truck.df.loc[0,'timestamp']
    return truck


def time_processing(df):
    print
    df['timestamp'] = df['timestamp'].apply(lambda x: datetime.datetime.strptime(x[:-6], '%Y-%m-%dt%H:%M:%S'))
    df['lat'] = df['lat'].astype(float)
    df['lng'] = df['lng'].astype(float)
    return df

def update_isin_target(df):
    def get_gps_distance(location, radi):
        print("check location ", location)
        # Fuso's target destination dictionary
        target_place = {}
        target_place['1'] = (35.50114245663584, 139.77058608966317)
        target_place['2'] = (35.55767062747489, 139.6647807694566)
        target_place['3'] = (35.47113783648265, 139.36696119089578)
        target_place['4'] = (35.52031899275968, 139.35217137718712)
        for i in range(1, 5):
            if (haversine(location, target_place[str(i)]) < radi):
                return i
        return 0


    radi = 0.7  # set geofence

    df['is_in_target'] = get_gps_distance(tuple(df[['lat','lng']].iloc[0].values), radi)

    return df


