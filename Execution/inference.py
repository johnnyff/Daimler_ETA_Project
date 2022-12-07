

def predict_model(df, model):
    using_predict_col = ['vehicleCode', 'lat', 'lng', 'velocity', 'is_in_target', 'total_distance', 'left_distance',
                         'time_cum_sum', \
                         'total_time', 'now_state', 'weekday', 'velocity_mean_sec', 'velocity_std_sec',
                         'velocity_mean_day', 'velocity_std_day']
    #res = model.predict(df[using_predict_col])
    #return res