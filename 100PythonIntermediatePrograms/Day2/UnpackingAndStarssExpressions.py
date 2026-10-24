# unpacking takes values out of a list, tuple, or dictionary and puts them into separate names.
# A * name collects any values left over; * and ** can also spread a list or dictionary into another place.

# first gets the first number, last gets the last, and middle collects everything between them into a list.
first, *middle, last = [10, 20, 30, 40, 50]
print(first, middle, last)

# Show the type of each result: first and last are integers; middle is a list.
print(type(first), type(middle), type(last))

# Put the two values on the right into the names on the left, in the same order.
a, b = 1, 2
print(a, b)

# Swap a and b in one line: a becomes 2 and b becomes 1.
a, b = b, a
print(a, b)

# Unpack a nested tuple: name gets "point", and x and y get 3 and 4.
name, (x, y) = ("point", (3, 4))
print(name, x, y)
print(type(x),type(y))


def total(*nums):
    # *nums gathers all the supplied arguments into a tuple; sum adds them together.
    return sum(nums)


# The * in this call spreads both lists into separate arguments: 1, 2, 3, 4, and 5.
print(total(*[1, 2, 3], *[4, 5]))

# ** spreads dictionary entries into a new dictionary. If a key appears twice,
# the value from the later dictionary (override) replaces the earlier one.
defaults = {"host": "localhost", "port": 0}
override = {"port": 9000, "debug": True}
config = {**defaults, **override}
print(config)

# items() provides each key and value; enumerate also gives each pair a number,
# starting at 1. The nested unpacking puts those three values into i, key, value.
# Talha enumerate() gives you the index (position) and value of each item.
# .items() gives you the key and value of each dictionary entry.
for i, (key, value) in enumerate(config.items(), start=1):
    print(config.items())
    # print(enumerate(config.items())) # was wanting to check
    print(i, key, value)

# A starred name collects the remaining letters. Here head gets the first letter
# and the unused letters are collected in a list named _.
head, *_ = "hello"
print(head)
