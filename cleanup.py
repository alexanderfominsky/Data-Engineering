import os
import time

# Путь к директории с файлами
directory = 'D:\Yeah Buddy\Pi\Farpost-Jupiter\data_slices\\'  
def cleanup_old_files():
    current_time = time.time()
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        # Проверка, является ли файл старше 5 минут
        if os.path.isfile(file_path) and (current_time - os.path.getmtime(file_path)) > 300:
            os.remove(file_path)
            print(f"Удален файл: {file_path}")

if __name__ == "__main__":
    while True:
        cleanup_old_files()
        time.sleep(300)  # 5 минут
