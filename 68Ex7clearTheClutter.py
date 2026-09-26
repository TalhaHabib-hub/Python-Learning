'''
write a program to clear the clutter inside the folder on your computer. 
you should use the os module to rename all the png images from 1.png all the way till n.png where n is the number of png files in that folder. Do the same for other file formats
''' 

import os 
import random

# if (not os.path.exists("ClutterClear")):
#     os.mkdir('ClutterClear')


for i in range(0,45):
    rand = random.choice(('ced','pse','dgr','rte','yde'))
    os.rename(f'ClutterClear/',f'ClutterClear/{i+1}.png')


# for i in range(0, 44):
#     os.rename(f"ClutterClear/Tutorial{i}",f"ClutterClear/Khan{i}")