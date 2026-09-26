with open("talha.txt") as p:
    print(p.read())
    print(p.readline())
    print(p.readline()) # returns as a function
with open('talha.txt','w') as p:
    p.writelines('34,67,23')
    p.writelines('\n34,123,23')
    p.writelines('\n34,67,322')
    p.writelines('\n345,67,23')

'''Talha Sir has mentioned here that we can do this task with loop'''
f = open('talha.txt','r')
while True:
    line = f.readline()
    print(line)
    if not line:
        print(line, type(line)) #  <class 'str'> befor the less then operator the line here is printed just a space and teh type is stirng because the string is returned when we use the function readline
        break
f.close()
f = open('talha.txt','r')
i = 0
while True:
    i = i + 1
    line = f.readline()
    if not line:
        break
    m1 = line.split(",")[0]
    print(line.split(','))
#['34', '67', '322\n'] <--- line.split(',')
    print('need to print 3:',[3,5,4][0]) # Sir harry has used this above type of logic
    m2 = int(line.split(",")[1])
    m3 = line.split(",")[2]
    print(f"Marks of student {i} in Math is : {m1*2}") # m1 is string but m2 is int
    print(f"Marks of student {i} in CS is : {m2*2}")
    print(f"Marks of student {i} in Eng is : {m3}")
f.close()

f = open('myfile.txt','w')
lines = ['line1\n','line9\n','line3\n','line4\n']
f.writelines(lines) # actually Talha this is one line but \n making it look 4 lines
# Talha very good you caught it you asked yourself how the list got written in the form of text as we see the result of the above code was this
'''
line1
line9
line3
line4
''' # but Talha how the list got like this so Talha here it is (the writlines function returns returns the list as string so implicity it type casting and below here you have shown that you got variable and type cast like the writelines function does you used the join function that converts the list into a stirng by joining the items of the list and when the list is converted the \n causes new line and that is how you found in the above task )
line = ''.join(lines) # me converting list into strings
print(line)
''' '''

