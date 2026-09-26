print("Hello world")
print(5)
print("Bye")

read_book_1 = True
read_book_2 = False
print(any([read_book_1, read_book_2]))  # True
print(all([read_book_1, read_book_2]))  # False

# complex numbers are the extension of real number system
numi = 3 + 2j
print(numi)
print("or")
print(complex(2, 4))
print(numi.real, numi.imag)
# the complex is function name while the real and imag are key words
print(abs(-244))
print(round(5.56))
print(
    round(5.56, 1)
)  # second arguments for rounding till how much nth digits we term normally as tenth place

# enums are readable name that are bound to a constant value
from enum import Enum


class State(Enum):
    inactive = 0
    active = 1


print(State.active)
print(State.active.value)  # 1
print(State(1))  # State.active
# 