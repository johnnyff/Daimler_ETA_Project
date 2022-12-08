

def predict_model(df, model):
    using_predict_col = ['vehicleCode', 'lat', 'lng', 'velocity', 'is_in_target', 'avg_total_distance', 'left_distance',\
                         'time_cum_sum','avg_total_time', 'now_state', 'weekday', 'velocity_mean_5sec', 'velocity_std_5sec',\
                         'velocity_mean_day', 'velocity_std_day']
    print(df.loc[0,using_predict_col].values)
    res = model.predict(df.loc[0,using_predict_col].values)
    return res