'''Recursion in Python'''
# Recursion is the process of defining something in terms of itself
# A physical world example would be to place two parallel mirrors facing each other. Any object in between them would be reflected recursively
'''Python Recursive Function'''
# In python, we know that a function can call other funcions. it is even possible for the function to call itself. these types of construct are termed as recursive functions.

def factorial(num):
    if num==0 or num==1: # num==0 only useful if we want to find factorial zero
        return 1
    else:
        return num * factorial(num-1)

# Driver code
num = 6
print("Number: ", num)
print("Factorial: ",factorial(num))

'''calculating of fibonachi'''
def fibonachi(number): # 0 1 1 2 3 5 8
    if number < 2:
        return 1
    else:
         return( fibonachi(number-1) + fibonachi(number-2))

number = 4
print(fibonachi(number))

'''
fib(4)---->fib(3)  + fib(2)----->  fib(1)  + fib(0)
    +       |_fib(2)  + fib(1)-->1   |_1       |_1
                |_fib(1)  + fib(0)
                    |_1         |_1
'''