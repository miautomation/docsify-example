#!/usr/bin/env python3

import glob
import os

PATH = "."

files = []

for x in os.walk(PATH):
    for y in glob.glob(os.path.join(x[0], '*.md')):
        files.append(y)
        files[-1] = files[-1].replace(".", "", 1)

sidebar_file = open('_sidebar.md', 'w')
name = "Home"
file = "/"
sidebar_file.write(f"* [{name}]({file})\n")


try:
    # files.remove("/README.md")
    files.remove("/_sidebar.md")
    # put any other files you want to remove here
except:
    pass

files.sort()

for file in files:
    if ".md" in file:

        name = file[1:-3]
        name = name.replace("/", "'s ")
        name = name.replace("_", " ")
        name = name.replace("-", " ")

        file = file.replace(" ", "%20")

        sidebar_file.write(f"* [{name}]({file})\n")

sidebar_file.close()

print("============================================================")
print("Sidebar:")
print("============================================================")
try:
    os.system("cat _sidebar.md")
except:
    print("Unable to `cat _sidebar.md`")
print("============================================================")