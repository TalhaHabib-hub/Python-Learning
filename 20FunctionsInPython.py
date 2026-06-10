# geometric mean is when we divide the product of two numbers with the sum of these numbers

def calculateGmean (a, b):
    mean = (a*b)/(a+b)
    print(f'The Geomatric mean of {a} and {b} is {mean}')

calculateGmean(4,3)
calculateGmean(7,3)
calculateGmean(4,3)
calculateGmean(9,3)

def greater(a, b):
    if a>b:
        print(f'{a} is greater')
    else:
        print(f'{b} is greater')
     
def islesser(a,b):
    pass # if you are wanting to write the code after anytime then you should use pass without it the interpreter will show error, it actually pass over me or pass to next.
     
def add():
    return 9

islesser(8,3)
greater(9,3)
print(add())