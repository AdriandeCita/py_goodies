# I often use this script to parse my playlists and
# save selected files from large discografies.
import os

playlist = input("Your .m3u playlist: ")
output_folder = input("Folder for music: ")

list_source = open(playlist, "r")

working_list = []
for l in list_source:
    if l[0] != "#":
        working_list.append(l[:len(l)-1])

if not os.path.exists(output_folder):
    os.makedirs(output_folder)

for file_entry in working_list:
    original_file = open(file_entry, "rb")
    new_file = open(
        os.path.join(output_folder, os.path.basename(original_file.name)),
        "wb")
    new_file.write(original_file.read())
    new_file.close()
    original_file.close()
