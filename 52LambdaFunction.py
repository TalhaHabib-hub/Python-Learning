'''use to write anonymous functions'''
# In python, a lamda function is a small anonymous function without name. it is defined using the lamda keyword and has the following syntax:
# lambda arguments: expression
# lambda function are often used in situations where a small function is required for a short period of time. They are commonly used as arguments to higher-order functions, such as map, filter and reduce.
# def double(x):
#     return x*2

'''Oo Talha here I am representing things for you look
just make the function name as a variable put the equal sign tell the interpreter it isn't a  variable bro it is lambda look here I am writing that for you baby now do nothing Talha just click a space type the parameter variable have : a semicolon now and write the task which you want the function to perform that will be returned without writing the return ya baby do one more for multiplying: and also don't care for the indentation
'''
multiply = lambda x    : x+x+x+x-3
division = lambda x    : x/3*6+x
mix      = lambda x,r,t: x*r*t
print('division      : ',division(5))
print('multplication : ',multiply(4))
print('mix           : ',mix(3,2,4 ))
# deal = lambda fx, i : 6 + fx(i) # TypeError: <lambda>() missing 2 required positional arguments: 'r' and 't'

'''here Talha jani I am going to tell you the concept: you can say hay bro (mean function take this function I want you to perform some task with this function too ok ealier I was giving you just variable now get function too bro)'''
#-------------------deal = lambda fx, i,j,k : 6 + fx(i,j,k)------------------------# 
'''or'''
def deal(x,i,j,k):
    return 6 + x(i,j,k)
print('dealing       : ',deal(mix, 3,4,3)) # this one is same as this below one
print('dealing       : ',deal(lambda x,r,t: x*r*t, 3,4,3))

'''Lambda functions are often used in situations where a small function is requires for a short period of time. They are commonly used as arguments to higher-order functions, such as map, filter, and reduce'''