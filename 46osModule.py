'''os module in python'''
# The os module in python is a built in library that provides functions for interacting with the operating system. It allows you to perform a wide variety of tasks, such as reading and writing files, interacting with the file system, and running system commands.
# Here are some common tasks you can perform with the os module:
# Reading and writing files The os module provides functions for openning, reading, and writing files.
# for example, to open a file for reading, you can ue the open function:
'''
import os

# Open the file in read-only mode
f = os.open("myfile.txt".os.O_RDONLY)

# Read the contents of the file
contents = os.read(f,1024)

#Close the file
os.close(f)'''

import os
# os.mkdir("DataTalhaOs")
# now I am wanting to make file for day hundred like our this course sir made this for us for that i will do this 
# Talha you first made the directry now again if you write the same instruction with somecode or just as it was you will recieve an error message the same name directory can't be made again twice for that message avoiding you would say

# if(not os.path.exists("DataTalhaOs")):
#    os.mkdir("DataTalhaOs")

# for i in range(1, 100):
#     os.mkdir(f"DataTalhaOs/Dar{i}")
    

# now let say I want to rename all my file

# for this I commented th line 25 and 26 and also commented the directory making code before these 2

# for i in range(1, 100):
#     os.rename(f"DataTalhaOs/Tutorial{i}",f"DataTalhaOs/Tutorial {i}")

# now lets say I am wanting to know that how many file are there in the directory
# for that I will do this

folders = os.listdir("DataTalhaOs")
# os.getcwd()
# os.chdir("/Users") # when I did this the directory changed the below codes were not running because we shifted into other directory
# os.getcwd() 

# print(folders)
#  # now I am wanting to print these folders one by one
# for folder in folders:
#     print(folder)
#     print(os.listdir(f"DataTalhaOs/{folder}")) # Talha notice that files are printed at some random pattern
# now lets do this Talha let make a file in the sub file of DataTalhaOs
if (not os.path.exists("Talha2")):
    os.mkdir("Talha2")
# for i in range(1,74):
#     os.mkdir(f"Talha2/{i}Talha.cpp")
# for i in range(1,74):
#     os.rename(f"Talha2/{i}Talha.cpp",f"Talha2/{i}S")


# print(os.listdir("Talha2"))
# for i in dir("Talha2"):
for i,b in enumerate(dir("Talha2")):
    if i<73:
        # print(os.listdir("Talha2"))
        print(os.listdir(f"Talha2/{i+1}S"))
