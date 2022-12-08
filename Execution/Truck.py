import util
import pandas as pd
import datetime
class Truck:
    def __init__(self,df,velocity_5sec_info, velocity_weekday_info):
        self.df= df
        self.prev_time = 0
        self.prev_timestamp = 0
        self.cum_distance =0
        self.cum_time = 0
        self.state_flag =0
        self.state=0
        self.cnt=0
        self.velocity_5sec_info = velocity_5sec_info
        self.velocity_weekday_info = velocity_weekday_info

    #def set_parameter(self,):
    def set_initial_timestamp(self, timestamp):
        if(self.prev_timestamp==0):
            self.prev_timestamp = datetime.datetime.strptime(timestamp[:-6],'%Y-%m-%dt%H:%M:%S')

    def set_rootName(self, name):
        self.root_name = name

    def set_journeyList(self, journey_list):
        self.journey_list = journey_list

    def get_truck_cum_distance(self):
        return self.cum_distance

    def get_truck_cum_time(self):
        return self.cum_time

    def get_state(self):
        return self.state

    def update_now_state(self):
        if(self.df.loc[0,'is_in_target']!=self.state_flag):
            self.cnt+=1
            self.state_flag= self.df.loc[0,'is_in_target']
            if(self.cnt%2==0):
                self.state=(self.state+1)%len(self.df['journey']);


