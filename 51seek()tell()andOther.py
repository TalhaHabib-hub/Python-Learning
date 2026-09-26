'''______________________seek() and tell() functions___________________________'''
# In python, the seek() and tell() functions are used to work with file objects and their positions within a file. These functions are part of the built-in io module, which provides a consistent interface for reading and writing to various file-like obects, such as files, pipes, and in-memory buffers.
'''____seek() function__'''
# The seek function allows you to move to the current position within a file to a specific point. The position is specified in bytes, and you can move either forward or  backward from the current position. for example:
with open('filekhan.txt','w') as F:
    print(type(F))
    list = ['kasa ho. ', 'we missed you allot, ','stay blessed']
    # F.write(list) # didnot worked
    F.writelines(list)
    # F.truncate(6)
    
with open('filekhan.txt', 'r') as f:
    print(f.tell()) # zeroth
    f.seek(18)
    print(f.tell()) # talha reading reached at 18th
    data = f.read(5)
    print(f.tell())  # reading reached at 23
    # Talha this gonna tell me till which oneth charachter does the reading goes
    print(data) # you (_you_) .. 'after' 18 read 5 characters
 # Talha here is something interesting for you if you have write something or already written but now if you want to trucate it or keep it to your desired number of characters just use the function truncate that will confined your text in the file to whatever number you want write that number in the paranthesis of the truncate function
  
