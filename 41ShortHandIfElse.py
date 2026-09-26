'''
There is alos a shorthand syntax for the if-else statment that can be used when the condition being tested is simple and the code blocks to be executed are short.
'''
a = 330
b = 3303
print("A")if a>b else print("=")if a==b else print("B")
a = input("hi talha!")
print("Talha") if a == "T" else print("saad") if a == "S" else print("no")
e = 943

# what i am saying here is do assign 9 to c if a > b if not (else ) do 0
c = 9 if e>b else 0
print(c)

                # we don't have to read the name of the variable as we do in normal way''''''''''''''''''''''''''|
#   result = value_if_true if condition else value_if_false
'''This syntax is equivalent to the following if-else statment'''
# if condtion:
#     result = value_if_true
# else:
#     result = value_if_false

'''
The shorthand syntax can be a convenient way to write simple if_else statments, especially when you want to assign a value to a variable based on a condtion. However, it is not suitabale for more complex situations where you need to execute multiple statments or perform more complex logic. In those cases, it's best to use the full if-else syntax'''

