from datetime import datetime, timedelta

def sum_time(time_list):
    total_time = timedelta()
    for time_str in time_list:
        time_obj = datetime.strptime(time_str, '%H:%M:%S')
        time_delta = timedelta(hours=time_obj.hour, minutes=time_obj.minute, seconds=time_obj.second)
        total_time += time_delta
    return str(total_time)

time_list = ['01:30:00', '02:15:30', '00:45:15']
total_time = sum_time(time_list)
print(total_time) # выведет '04:30:45'