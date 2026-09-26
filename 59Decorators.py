'''_______Python decorators_________
these are a powerful and versatile tool that allow you to modify the behavior of functions and methods. They are a way to extend the functionality of a function or method without modifiying its source code.
A decorator is a function that takes another funtion as an argument and returns a new function that modifies the behavior of the oringinal function. The new function is often refered to as a "decorated" function. The basic syntax for using a decorator is the following:
@decorator_function 
def my_function():
    pass
    
The @decorator_function notation is just a shorthand for the following code:

def my_function():
    pass
my_fuction = decorator_function(my_function)()

Decorator are often used to add funcitonality to functions and methods, such as logging, memorization, and access control

'''

def greet(fx):
    def mfx(*args,**kwargs): # Talha you know that the first one gets the arguments as a tuple while the other one gets as a dictionary
        print("Good Mornig")
        fx(*args, **kwargs)
        print("Thanks for using this function")
        print('________________________________')
    return mfx

@greet
def hello():
    print("Hello world")

# |Talha you can't use this with greet function because greet only gets a function with no arguments in this case (a  I said befor because the greet function was not defined for the functions with arguments
@greet
def add(a, b):
    print(a + b)

hello()

add(5,6)
# greet(add)(3,54) 
'''Talha you are intelligent guy look the above line you have the alternative of it just write @greet before the function which you are wanting to modify and then when ever you have to call the function in modified form just called the function and there is no need of writing the function (The greet()() again and again'''
# greet(hello)() # Talha writing this is the same as writing @ greet after the greet(funtion definition) also Talha you were thinking that the calling to the greet as in the begining of this line is little bit unusual but here is the reason the first paranthesis will get the function name and the second one will get the arguments also talha don't forget the greet function to take them too that is why the function  is additionally added like the quarks and args but here is still question in my mind why not just the x why *x or **x I know I had read this ones but at that time I was calling the function with tuples or dictionary , what clicking my mind is that I am not using here any sort of tuples or dictionary the most likely is that using *x or **x can may make the function to catch any sorts of object the other thing is may be the objects are casting into the tuple but what the dictionary takers is doing there if the case is this

add(4,3)

'''Python decorator are a powerful and versatile tool that allow you to modify the behavior of functions and methods. They are a way to extend the functionality of a function or method without modifying its source code
A decorator is a function that takes another function as an agrument and returns'''

'''One common use of decorators is to add logging to a function. for example, you could use a decorator to log the arguments and return value of a function each time it is called'''

import logging

def log_function_call(func):
    def decorated(*args, **kwargs):
        (logging.info(f'Calling {func.__name__} with args = {args}, kwargs = {kwargs}'))
        result = func(*args, **kwargs)
        logging.info(f'{func.__name__} returned {result}')
        return result
    return decorated
@log_function_call
def my_function(a,b):
    return a + b

print(my_function(4,2))

'''In this example, the log_function_call decorator takes a function as an argument and returns a new function that logs the function call before and after the original function is called'''


'''Conclusion'''
'''Decorators are a powerful and flexible feature in pyton that can be used to add functionality to functions and methods without modifying their source code. They are a great tool for seperating concerns, reducing code duplication, and making your code more readable and maintable, and extendable
'''
def adder(fx):
    def decorater(*i):
        print("|Hey Talha owned this|")
        fx(*i)
        print("|have a good day ")
        print(decorater)
    return decorater
@adder
def voice(*i):
    print(f"________Talha______{i}__")
voice(4,3,4) # so this function is sending tuple what about dictioanary lets look at that too
voice("name","Talha") # this is still a tuple not a dictionary

'''the importance of deocorator functions
most of the time we feel the need of it lets say you have made website and there are alots of function for different inteactors with the website for example for the teenagers for old for the workers for the alleeds lets say there are 100 of sort people and these functions are dealing with the people for which these are written but now you want that I want all these function to greet my users and also thanked them after the usage, now it is heavy sort of work that you will modify each function to make things easier for you the decorator is used so what you have to do is just make a function that takes a function and when you call your function that will be modified by this one automatically the old version will not run as it was just write the @funcName above the function which you want to modify now going back how the decorator function is ? so after makiing a function that gets a function inside this function write whatever you want to modify about that and also called the parametered function where ever you want and then return this function back to the decorator function you task is done lets have a look for it'''

# lets say first we have these funcitons
def decorating(f):
    def decoration(*x):
        print("Hi wilcome Talented")
        f(*x)
        print("Talha  got brilliance")

@decorating
def name(*x):
    print(f'welcome {x}')
@decorating
def teen(*x):
    print(f' welcome teen name : {x}')
@decorating
def nameold(*x):
    print(f'welcome old name:{x}')
@decorating
def young(*x):
    print(f' welcome young name : {x}')

name('Talha')
print('_________________')
nameold('yasir')
print('_________________')
young('khan')
print('_________________')
teen('jhon')

