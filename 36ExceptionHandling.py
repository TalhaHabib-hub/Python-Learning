'''-------------Exception Handling--------------------------'''
# Exception handling is the process of responding to unwanted or unexpected events when a computer program runs. Exception handling deals with these events to avoid the program or system crashing, and without this process, exception would disrupt the normal operation of a program.
'''-------------Exceptions in Python--------------------------'''
# Python has many built-in exceptions that are raised when your program encounters an error( something in the program goes wrong).

# When these exceptions occurs, the python interpreter stops the current process and passes it ot the calling process until it is handled. If not handled, the program will crash.
'''-------------Python try...except--------------------------'''
# try.... except blocks are used in python to handle errors and exceptions. The code in try block runs when there is no error. if the try block catches the error, then the except block is executed.

# a = int(input("Enter a number: "))
# for i in range (1,11):
#     print(f'{a} X {i} = {a*i}')

# but what if input isn't integer
a = (input("Enter a number: "))
try: # try it if it not really works except will be executed
    for i in range (1,11): 
        print(f'{int(a)} X {i} = {int(a)*i}')
except:
    print("Invalid syntax")#--------------------------|
# except Exception as e:#-----------------------------| used to handle problem
#     print(e)

print("Some important lines of code")

b = input("Enter a number: ")
print('here is the multiplication of numbers from zero to ',b)
 
try:
    for i in range(int(b)):
        print(f'{i} X {2} = {i*2}')
except:
    print("Invalid syntax!")


'''-------------------------multiple buil-in exceptions---------------------------'''
try:
    num = int(input('Enter an integer: '))
    a = [6, 4]
    print(a[num])
except ValueError: # put the value like other then int
    print('Number entered is not an integer')
except IndexError: # put the value like
    print("Index Error")


# Talha this below one is showing error
num = int(input('Enter a character'))
char = 'rt'
try:
    print(num + char)
except:
    print("Error")