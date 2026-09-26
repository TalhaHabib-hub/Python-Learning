class Math:
    def __init__(self, num):
        self.num = num

    def addtoNum(self, n):
        self.num += n

    @staticmethod
    def add(a , b): # no need to put self argument
        return a + b

# result = Math.add(1,2)
# print(result)
a = Math(5)
print(a.num)
a.addtoNum(6)
print(a.num)
print(a.num,2) # how this one behaves
print(Math.add(4,4))
print(a.add(4,4))
# print(add(4,4)) wrong

'''Static methods in python are methods that belong to a class rather than an instance of the class. They are defined using the @staticmethod decorator and do not have access to the instance of the class (i.e. self). They are called on the class itself, not on an instance of the class. Static methods are often used to create utility functions that don't need access to instance data

In the code, the add method is a static method of the Math class. It takes two parameters a and b and returns their sum. The method can be called on the clas itself, without the need to create an instance of the class'''