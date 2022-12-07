import util
import pandas as pd
import datetime
class Truck:
    def __init__(self,df):
        self.df= df
        self.cum_distance = 0
        self.cum_time =0
        self.prev_time = 0
        self.prev_distance =0
        self.prev_timestamp = 0

    #def set_parameter(self,):
    def set_initial_timestamp(self, timestamp):
        self.prev_timestamp = datetime.datetime.strptime(timestamp[:-6],'%Y-%m-%dt%H:%M:%S')

    def set_rootName(self, name):
        self.root_name = name

    def set_journeyList(self, journey_list):
        self.journey_list = journey_list

    def get_truck_cum_distance(self):
        return self.cum_distance

    def get_truck_cum_time(self):
        return self.cum_time

    def update_now_state(self,df):
        return df
