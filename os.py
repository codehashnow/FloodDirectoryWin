import os 
import time

def create_folders(base_path, duration):
    start_time = time.time()
    count = 0

    while time.time() - start_time < duration:
        folder_name = f"FUCKYOU{count}"
        folder_path = os.path.join(base_path, folder_name)
        os.makedirs(folder_path, exist_ok=True)
        print(f"Created: {folder_path}")

        # Создаем папку внутри текущей папки
        inner_folder_name = f"FUCKYOU{count}"
        inner_folder_path = os.path.join(folder_path, inner_folder_name)
        os.makedirs(inner_folder_path, exist_ok=True)
        print(f"Created: {inner_folder_path}")
        count += 1

# Укажите путь к папке, в которой будут создаваться новые папки
base_path = "C:/SHOWME"
create_folders(base_path, 50)
