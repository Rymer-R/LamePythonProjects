#4th Project for Lame python projects
#Simple script or program to take screenshot using pyscreenshot ;-;

import pyscreenshot as imagegrab
import os

#Capturing full screen

# grab fullscreen
im = imagegrab.grab()
CurrentWorkingDirectory = os.getcwd()
FilesInDirectory = os.listdir(CurrentWorkingDirectory)
# managing the name of the screenshot files going to be saved
filename = "fullscreen"
dup_count = 0
while True:
    if dup_count ==0:
        final_name = f"{filename}.png"
    else:
        final_name = f"{filename}{dup_count}.png"
    if final_name not in FilesInDirectory:
        filename = final_name
        break
    dup_count += 1
# save image file
print("Taking screenshot fullscreen")
im.save(final_name)
print(f"File saved to {os.path.join(CurrentWorkingDirectory, filename)}")