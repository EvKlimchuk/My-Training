import os
import time

directory = '.'

for root, dirs, files in os.walk(directory):
    for file in files:
        filepath = os.path.join(root, file)
        # print(filepath)
        filetime = os.path.getmtime(filepath)
        formatted_time = time.strftime("%d.%m.%Y %H:%M", time.localtime(filetime))
        filesize = os.path.getsize(filepath)
        parent_dir = os.path.dirname(filepath)
        abs_path = os.path.abspath(filepath)

    print(f'File detected: {file}, Path: {filepath}, Size: {filesize} bytes, Time of change: {formatted_time},'
          f'Parent directory: {parent_dir}')

