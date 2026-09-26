'''----------How importing in python workd---------------'''
# Importing in python is the process of loading code from a python module into the current script. This allows you to use the functions and variables defined in the module in your current script, as well as any additional modules that imported module may depend on.
# To import a module in python, you use the import statement followed by the name of the module. For example, to import the math module, which contains a varity of mathematical functions, you would use the following statments
''' import math '''
# Once a module is imported, you can use any variables defined in the module by using the dot notation. for example, to use sqrt funtion from the math module, you would write
'''
import math

result = math.sqrt(9)
print(result) # Output 3.0

'''
#------------------From keyword--------------
# you can also import specific fuctions or variables from a module using the from keyword. for example, to import onlyt the sqrt function from the math module, you would write:
'''
from math import sqrt
result = math.sqrt(9)
print(result) # Output: 3.0
'''

# import pandas
# pandas.read_csv()

# import math
# math.floor(4.2324)
'''
from math import sqrt , pi
# result = math.sqrt(9) # now Talha you will not write the module name
result = sqrt(9)
print(result,pi) # Output: 3.0

'''


'''----------------Importing everything----------------'''
# It's also possible to import all functions and variables from a module using the *wildcard. However, this is generally not recommended as it can lead to confusion and make it harder to understand where specific functions and variabless are coming from

from math import *
result = sqrt(9)
print(result)


# python also allows you to rename imported modules using keyword. This can be useful if you want to use a shorter or more descriptive name for a module, or if you want to avoid naming conflicts with other modules or variables in your code
'''-------------using as key word----------------'''
from math import sqrt as sq 
print(dir(sq))
# also I can do like this
import math as MT
# ty = MT.pi()  # wrong because pi is a variable not a function
ty = MT.pi
print(ty)

result1 = sqrt(9)
result = sq(5)
print(result1) # Output: 3.0
print(result) # Output: 3.0

'''-----------------The dir function--------------------'''
# Finally, python has a built-in function called dir that Talha you can use to view the names of all the functions and variables defined in a module. This can helpful for exploring and understanding the contents of a new module
import math
print(dir(math))
print(MT.nan,type(math.nan))
'''Talha remember this it didn't told you what is nan just printed nan but why'''
# This will output a list of all the names defined in the math module, including functions like sqrt and pi, as well as other variables and constants

'''
In summary, the import statment in python allows Talha you to access the functions and variables defined in a module from within your current script. You Talha can import the entire module, specific functions or variables, or use the*wildcard to import everything. you can also use the as keyword to rename a module, and the dir function to view the contents of a module'''


'''This was my first module you can say jhoni'''
# from mymodule import welcome,Truey # this one will work
# from mymodule import *  . 
# import mymodule # this one is not working because at that time i have to write the name of the module and '.'
import mymodule
mymodule.welcome()
print(mymodule.Truey)