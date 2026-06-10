'''_______________________________Finally Clause_________________________________'''
'''
The finally code block is also a part of exception handling. when we handle exception using the try and except block, we can include a finally block at the end. The finally block is always executed, so it is generally used for doing the concluding tasks like closing file resources or closing database connection or may be ending the program execution with a delightful message
'''
'''
Syntax:
try:
    #statments which could generate
    #exception
except:
    #solution of generated exception
finally:
    #block of code which is going to 
    #execute in any situation
'''
'''
The finally block is executed irrespective of the outcome ot try........except.....else blocks
One of the important use cases of finally block is in a function which returns a value'''

try:
    l = [1,4,5,3]
    i = int(input('Enter the index'))
    print(l[i])
except:
    print("some error occured")
finally:
    print("I am always executed") # Talha what is the difference between using finally and just writing another statment out side the hold of except mean without indentation, To answer it I am wrapping it in a function


def func():
    try:
        l = [3,4,2,4]
        i = int(input('Enter the value of index Sir.'))
        print(l[i])
        return "how giya bina error ka"
    except:
        return "jani sorry!"
    # print("hi Talha kasa ho") # this one is not gonna execute but
    finally:
        print("Hi kia hal chal!")


a = func()
print(a)