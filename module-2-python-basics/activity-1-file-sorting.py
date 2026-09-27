"""
Module 2 — Activity: File Sorting with os and shutil
Student: [Justin Quiambao]
Date: [September 27, 2026]

============================================
WHAT DID YOU BUILD? (explain in your own words)
============================================
[I built an Python script that automatically organizes files inside
a folder based on file extensions. The Python script uses the os module
to examine every item, inside the folder and the shutil module to
move each file into a sub-folder named after its extension.
For example all.png files go into a folder called "png". If
the destination folder does not already exist the Python script
automatically creates the destination folder before moving the file.]


============================================
KEY VOCABULARY
============================================
- os module: a built-in Python module that lets a program interact
with the operating system, such as listing the contents of a
folder or checking whether a path exists.

- shutil module: a Python module used for higher-level file
operations, such as moving or copying files.

- file path: the location address of a file on the computer
for example "test_folder/notes.txt".

- directory: another word, for folder.
(add more as needed) 


============================================
YOUR SCRIPT
============================================
Paste the code you already wrote for this activity below.
"""

import os
import shutil

source_folder = r"C:\Users\PC\Downloads\jus\jus\test_folder"

for filename in os.listdir(source_folder):
    file_path = os.path.join(source_folder, filename)

    if os.path.isfile(file_path):
        extension = filename.split(".")[-1]
        dest_folder = os.path.join(source_folder, extension)

        if not os.path.exists(dest_folder):
            os.makedirs(dest_folder)

        shutil.move(file_path, os.path.join(dest_folder, filename))

# --- paste your existing code here ---


"""
============================================
A MISTAKE I MADE (or one I want to avoid)
============================================
[At first I renamed my test files using File Explorer for example changing New Text Document txt to image png 
but I didn't realize that Windows hides file extensions by default Because of this everything 
I renamed actually became image png txt behind the scenes I could only see image png but the true extension was still txt 
When I ran the script all the files ended up in the txt folder of their correct extension folders 
I noticed this because the Type column for every file in File Explorer showed Text Document To fix it
I had to enable File name extensions, in the View settings first then rename the files correctly before running the script again]


============================================
HOW THIS CONNECTS TO SOMETHING ELSE
============================================
[Automation scripts work similarly to automation scripts in everyday life. 
For example if you have a downloads folder of different file types you could build an automation script that sorts them automatically.
I also learned that it is very important to verify your data, such as the filename before relying on an automation script. 
A small detail, such, as a file extension can affect the entire result.]
"""
