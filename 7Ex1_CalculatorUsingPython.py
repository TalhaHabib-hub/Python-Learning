print(" 5 + 6 = ", 5+6)
print(" 5 - 6 = ", 5-6)
print(" 5 * 6 = ", 5*6)
print(" 5 / 6 = ", 5/6)
print(" 5 // 6 = ", 5//6) # floor division # it will divide the same way as / but will remove the decimal portion
print(" 5 % 6 = ", 5%6)
print(" 5 ** 6 = ", 5**6)

# enums are readable names that are bound to a constant value
from enum import Enum

# initializing an enum 
class State(Enum):
    INACTIVE = 0
    ACTIVE = 1

print(State.ACTIVE.value) # 1
print(State['ACTIVE']) # State.ACTIVE
print(State['ACTIVE'].value)# 1
print(State(1))# State.ACTIVE
print(State.ACTIVE)# State.ACTIVE

# basically Talha this is the only way to create a constant in python
# some people use enums to create constant than no body can change them
print(State)
# we can find all the possible values for an enums
print(list(State))
# also we can find the length of enum
print(len(State))