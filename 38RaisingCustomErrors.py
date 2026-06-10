a = int(input("Enter any value between 5 and 9"))
 
if not(a>5 and a<9):
    raise ValueError("Value should be between 5 and 9")

'''____________________Raising Custom Errors__________________________'''
'''
In python, we can raise custom errors by using the r a i s e keyword'''

salary = int(input("Enter salary amount: "))
if not 2000 < salary <5000:
    raise ValueError('Not a valid salary!')

'''
In the previous tutorial, we learned about different built-in exception in Python and why it is important to handle exceptions. However, sometimes we may need to create our own custom exceptions that serve our purpose.

____________________Defining Custom Exceptions_____________________
In Python, we can define custom exceptions by creating a new class that is derived from the built-in Exception class.

Here's the syntax to define custom exceptions:
'''
'''
class CustomError(Exception):
    # code ..........
    pass

try:
    # code ..........

except CustomError:
    # code ..........

'''

s = input("only write 'quit'")
if not(s == 'quit' ):
    raise ValueError("value should only be quit")