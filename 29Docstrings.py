'''---------------------------Docstring and PEP 8---------------------------------'''
'''
Python docstrings are the string literals that appear right after the definition of a function, method, class, or module.
'''
def square(n):
    '''Takes in a number n, returns the square of n'''
    print(n**2)
square(5)
print(square.__doc__)

'''
Comments vs-----------------------Docstrings------------------------------
Comments are descriptions that help programmers better understand the intent and functionality of the program. They are completly ignored by the python interpreter
-------------------------------but------------------------------
Docstring are strings used right after the declaration of a function, before the function definition method, class or module(Like in the above example). They are used to document our code.
we can access these docstrings using doc attribute as (functionName.__doc__)


--------------------------PEP-8 python enhacement proposal---------------------
PEP 8 is a document that provides guidelines and best practices on how to write python code. It was written in 2001 by Guido van Rossum, Barry Warsaw and Nick Coghian. The primary focus of PEP 8 is to improve the readability and consistency of Python code.
There are several of PEPs out there. A PEP is a document that describes new features proposed for python and documents aspects of Python, like design and style, for the community

----------------------------Zen of Python---------------------------------
run this on terminal
import this
'''
