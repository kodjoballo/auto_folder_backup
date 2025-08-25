# 💾 Auto Folder Backup

## 📌 Description
This project automatically **backs up a folder** to a destination directory every day at a scheduled time.  
It creates a new backup folder labeled with the current date, ensuring that daily backups are organized chronologically.  

Uses:
- **`os`** → filesystem operations  
- **`shutil`** → copying entire folders  
- **`datetime`** → timestamping backups with the current date  
- **`schedule`** → running automated tasks at a specific time  

---

## 🚀 How to Run

### 1. Install Dependencies
This project uses the [`schedule`](https://pypi.org/project/schedule/) library:
```js
pip install schedule

```


### 2. Configure Source & Destination

In main.py, set your source and destination directories:

```js
source_dir = "C:\\Users\\ian\\Downloads\\Space Invaders Game"
destination_dir = "H:/Projet/Python Files/backup"
```
but of course, the this can be changed as per your preferences.

### 3. Set Backup Time

Update the time string (HH:MM format):

```js
schedule.every().day.at("16:56").do(lambda: copy_folder_to_directory(source_dir, destination_dir))

Example:

"09:00" → runs daily at 9:00 AM

"23:30" → runs daily at 11:30 PM

### 4. Run the Script

From the project folder:

```js
python.exe auto_folder_backup.py
```

The program will keep running in the background, checking once per minute.

### 📂 Example Output

If run on 2025-08-24, the backup folder will look like:

```js
backup/
└── 2025-08-25/
    └── (copied contents of source folder)
```
### 🖼️ Screenshot
<p align="center">

![image alt](https://github.com/kodjoballo/auto_folder_backup/blob/main/auto_folder_backup_1.png?raw=true)

</p>

And source copied in the backup folder specified.

<p align="center">

![image alt](https://github.com/kodjoballo/auto_folder_backup/blob/main/auto_folder_backup_2.png?raw=true)

</p>

### 📚 Concepts Used

Automating tasks with the schedule module

File system operations with os and shutil

Date-based folder naming with datetime

Infinite loop & delays with time.sleep()


### ⚠️ Notes

If the backup folder for today already exists, the script will skip copying.

Keep the script running in the background to ensure daily backups are created.

You can use Task Scheduler (Windows) or cron (Linux/Mac) to launch the script automatically at startup.

### Source code 👇 ☺️

[source_code](https://github.com/kodjoballo/auto_folder_backup/blob/main/auto_folder_backup.py)

