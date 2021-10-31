import os
import shutil

source= input("ENTER SOURCE FOLDER NAME: ")
destination= input("ENTER DESTINATION FOLDER NAME: ")
source=source+'/'
destination= destination+'/'

num=os.listdir(source)
for file in num:
    shutil.move((source+file),destination)