import time

print("Сейчас:", time.ctime())
time.sleep(2)

named_tuple = time.localtime() # получить struct_time
time_string = time.strftime("%m/%d/%Y, %H:%M:%S", named_tuple)



print("Через 2 секунды:", time.ctime())
print("с настройкой формата:", time_string)
