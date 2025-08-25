import os   # who stands for operation system
import shutil  # who's gonna do so copy operation for us
import datetime
import schedule
import time

source_dir = "C:\\Users\\ian\\Downloads\\Space Invaders Game"
destination_dir = "H:/Projet/Python Files/backup"

def copy_folder_to_directory(source, dest):
    today = datetime.date.today()
    dest_dir = os.path.join(dest, str(today))
    try:
        shutil.copytree(source, dest_dir)
        print(f"folder copied to the destination directory")
    except FileExistsError:
        print(f"Folder already exists in : {dest} ")

# Now we want to schedule this every day at a certain time

schedule.every().day.at("16:56").do(lambda: copy_folder_to_directory(source_dir, destination_dir))

while True:
    schedule.run_pending()
    time.sleep(60)


