# This downloads empty blank project from gitHub.
# It initializes your new project with it and creates
# additional folders
#
# To call it from everywhere, simply move html_init and html_init.py
# to /bin (on linux)
import os
import sys
import shutil

if (len(sys.argv) - 1):
    output_folder = str(sys.argv[1])
else:
    output_folder = input("Project folder name: ")
os.system("git clone https://github.com/AdriandeCita/blank_html_project.git " + output_folder)


folders = [
    "images",
    "fonts"]

for f in folders:
    os.makedirs(output_folder + "/" + f)

shutil.rmtree(output_folder + "/" + ".git")
