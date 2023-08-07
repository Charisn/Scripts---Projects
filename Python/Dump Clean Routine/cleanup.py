import os
import sys
sys.executable
import schedule
import time
import shutil

# Function to clear the downloads folder
def clear_downloads_folder():
    folder_path = 'C:/Users/Charis/Downloads'
    file_list = os.listdir(folder_path)
    for file_name in file_list:
        file_path = os.path.join(folder_path, file_name)
        if os.path.isfile(file_path):
            os.remove(file_path)

# Function to clear the recycle bin
def clear_recycle_bin():
    os.system('powershell.exe -command "Clear-RecycleBin -Force -ErrorAction SilentlyContinue"')

# Function to clear temporary files
def clear_temp_files():
    temp_path = 'C:/Users/Charis/AppData/Local/Temp'
    shutil.rmtree(temp_path, ignore_errors=True)
    os.makedirs(temp_path, exist_ok=True)
clear_temp_files()
clear_downloads_folder()
clear_recycle_bin()
# Schedule the tasks
schedule.every(4).hours.do(clear_downloads_folder)
schedule.every(4).hours.do(clear_temp_files)
schedule.every(4).hours.do(clear_recycle_bin)

# Infinite loop to keep the script running
while True:
    schedule.run_pending()
    time.sleep(1)
