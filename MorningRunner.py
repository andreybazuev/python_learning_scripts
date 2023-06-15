start_time_hour = 6.52    #время старта в часах
light_temp_speed = 8.15   #скорость легкого темпа (км/мин) 
average_temp_speed = 7.12 #скорость среднего темпа (км/мин)

time_hours = int (start_time_hour)  #отбросим дробную часть
time_minuts = int (round (start_time_hour % time_hours * 100, 0)) #отбросим целую часть
hours_to_minuts = time_hours * 60 + time_minuts #преобразуем время старта в минуты

#def time_to_seconds(minuts, seconds):     #Функция перевода времени
#    total_seconds = minuts * 60 + seconds
#    return total_seconds

light_temp_minuts = int (light_temp_speed)
light_temp_seconds = int (round (light_temp_speed % light_temp_minuts * 100, 0))
light_minuts_to_seconds = light_temp_minuts * 60 + light_temp_seconds

average_temp_minuts = int (average_temp_speed)
average_temp_seconds = int (round (average_temp_speed % average_temp_minuts * 100, 0))
average_minuts_to_seconds = average_temp_minuts * 60 + average_temp_seconds

total_running_time_sec = light_minuts_to_seconds * 2 + average_minuts_to_seconds * 3  #по условию задачи 2 км - легкий и 3 км - средний темп.
total_running_time_min = total_running_time_sec // 60
sec = total_running_time_sec % 60

minuts_total = hours_to_minuts + total_running_time_min
hours_return = minuts_total // 60
minuts_return = minuts_total % 60
print (f'Бегун вернулся домой в {hours_return} часов {minuts_return} минут {sec} секунд')