# f = open('myfile.txt') # this will work because by default the mode will be r
f = open('myfile.txt','r')
# print(f) #<_io.TextIOWrapper name='myfile.txt' mode='r' encoding='cp1252'> // there is no reason to print this
print(f.read())
# print(f.write("hi jani")) #io.UnsupportedOperation: not writable
f.close()
# print(f.read()) #ValueError: I/O operation on closed file.
# Talha if you have opened in a read or write mode you can't use  write and read command respectively

# Talha the above one is going to through error if the file isn't present but if we use the write mode even if the file doesn't exists the file will be made and the program will not show an error
file = open('talha.txt','w')
# I ran it didn't shown any error and made the file for me
# print(file.read()) 
sent = "Islam ka hero bananga InshAllah."
print(file.write(sent)) # so Talha doing this will overwrite whatever is written in the opened file in to the (file variable) and append is used Talha when you don't want to overwrite what is already written
# close("talha.txt")  # don't do this 
file.close() # instead do this
# print(file.read()) # you can't use talha when you openend in write mood
 
#  Talha without the above codes the word text is appending everytime but not when the code are present I don't know why it is.
fileO = open("talha.txt","a")
fileO.write("\naaj tum Yada bahisaab aya Talha.")
fileO.close()
fileO = open("talha.txt","a")
fileO.write("\naaj tum Yada bahisaab aya Talha.")
fileO.close()

# but now Talha it is like booring man opening a file and then storing it in a variable the another seperate statment of reading or writing and alos closing everytime, to solve your this issur Talha here is the trich
with open('talha.txt','a') as f:
    f.write("\nHey Jani may You have a fortuner")
# fileO.close()
# print(fileO.readline()) #io.UnsupportedOperation: not readable

# file3 = open("talha.txt",'x')  #FileExistsError: [Errno 17] File exists: 'talha.txt'
'''------------------------Modes in file----------------------'''
'''
there are various mode in which can open files.
1. read(r)   : opens file for reading only and gives and error if file doesn't exist.This is the default mode if no mode is passed as a parameter
2. write(w)  : opens the file for writing only and creates new file if doesn't exist.
3. append(a) : This mode opens the file for appending only and creates a new file if the file doesn't exits
4. create(x) : This mode creates a file and gives an error if the file alreay exists
5. text(t)   : Apart form these modes we also need to specify how the file must be handled. t mode is used to handle text  files. t refers to the text mode. There is no difference between r and rt or w and wt since text mode is the default. The default mode is 'r'(open for reading text, synonym fo 'rt)
binary(b)    : used to handle binary files(images, pdfs, etc)'''