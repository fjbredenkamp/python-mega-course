#4 modules you should learn: csv, glob, webbrowser, shutil

import glob

myfiles = glob.glob("../files/*.txt")

for filepath in myfiles:
    with open(filepath, 'r') as file:
        print(file.read().title())
        