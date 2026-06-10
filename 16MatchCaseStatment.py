x = int(input('Enter the value of x '))
# x is the variable to match
match x:
    # if x is 0
    case 0:
        print("x is zero")
    # case with if-condition
    case 4 if x % 2 == 0:
        print("x % 2 == 0 and case is 4")
    # Empty case with if-condition
    case _ if x < 10:
        print("x is < 10")
    # default case( will only be matched if the above cases were not matched)
    # so it is basically just an else:
    case _:
        print(x)
'''

Talha remember that no break statment is used 
That's correct!That's correct! In Python's match statement (introduced in Python 3.10), there is no need for break statements between cases.
In C++ (and C), switch cases fall through to the next case by default, so you need break to stop execution.

x = 4

match x:
  
    case 0               :
        print("x is zero")
  
    case 4 if x % 2 == 0 :
        print("x % 2 == 0 and case is 4")
 
    case _ if x < 10     :
        print("x is < 10")

    case _:
        print(x)
'''
x = int(input("what is your age: "))

match x:
    case 18:
        print("today you became eligible for voting")
    case x if x>18 and x<140:
        print("Yes you can vote")
    case x if x<18 and x>0:
        print("you can't vote")
    case _:
        print("Yes are not in this world")
