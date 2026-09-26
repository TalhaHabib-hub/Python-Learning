
# '''______________Getter___________________
# Getters in python are methods that are used to access the values of an object's properities. They are used to return the value of a specific prperty, and are typically defined using the @property decorator. Here is an example of a simple class with getter method'''

# class MyClass:
#     def __init__(self,value):
#         self._value = value
#         print(self._value)
#     def show(self):
#         print(f'value is {self._value}')
#     @property # commenting this line #AttributeError: 'function' object has no attribute 'setter'
#     def value(self):
#         return 10 * self._value
    
#     @value.setter
#     def value(self, new_value):
#         self._value = new_value/10


# obj = MyClass(10)
# obj.value = 43  #error
# # obj._value = 43
# print(obj.value) #<bound method MyClass.value of <__main__.MyClass object at 0x00000206C84786E0>>   # this is without line 14
# obj.show()
# print(obj.value) #<bound method MyClass.value of <__main__.MyClass object at 0x00000206C84786E0>>   # this is without line 14
# '''kisi bhi function ka return value ko aik object ki property ki tarah istimaal karsakta han oor set bhi karsakta han'''

class MyClass:
    def __init__(self, value):
        self._value = value

    def show(self):
        print(f"Value is {self._value}")

    @property
    def ten_value(self):
        return 10* self._value
    
    # @ten_value.setter
    # def ten_value(self, new_value):
    #     self._value = new_value/10

obj = MyClass(18)
obj.ten_value = 81
print(obj.ten_value)
obj.show()

#81.0
# Value is 8.1


