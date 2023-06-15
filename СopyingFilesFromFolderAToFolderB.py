import shutil
import os

# путь к папке, из которой нужно скопировать файлы
source_folder = r'C:\1111\TOKENS'

# путь к папке, в которую нужно скопировать файлы
destination_folder = r'C:\1111\TOKENS_2'

# Получаем список файлов в папке "a"
files = os.listdir(source_folder)

# Копируем каждый файл из папки "a" в папку "b" с добавлением содержимого
for file in files:
    # Формируем полный путь к файлу в папке "a"
    file_path_a = os.path.join(source_folder, file)
    
    # Формируем полный путь к файлу в папке "b"
    file_path_b = os.path.join(destination_folder, file)
    
    # Копируем файл из папки "a" в папку "b" с добавлением содержимого
    shutil.copy2(file_path_a, file_path_b)


