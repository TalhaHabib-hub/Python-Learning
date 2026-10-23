# A comprehension makes a new collection in one short expression by working through items one at a time.
# we can add a condition to keep only some items, choose between values, or use more than one loop.

# What I learned in this program:
# - Use range() to create a sequence of numbers.
# - Use list comprehensions to make lists, filter values, and label items.
# - Use dictionary and set comprehensions to organize unique or paired results.
# - Create a nested list and flatten it into one list.
# - Print the results to see what the program created.

# Set up a counting sequence from 1 to 10. Python stops before 11.
nums = range(1, 11)
# Turn the sequence into a list so the actual numbers are printed.
print(list(nums))
# Multiply each number by itself and put the answers in a list.
squares = [n**2 for n in nums]
# Pick out the numbers that divide evenly by 2.
evens = [n for n in nums if n % 2 == 0]
# Give every number an "even" or "odd" label.
labels = ["even" if n % 2 == 0 else "odd" for n in nums]
# For numbers 1 to 5, multiply each number by itself three times.
# Store each number beside its answer; numbers 6 to 10 are left out.
cubes = {n: n**3 for n in nums if n <= 5}
# Count the letters in each word. Keep each length only once.
lengths = {len(w) for w in ["apple", "fig", "kiwi", "plum", "pear"]}
# Make a small multiplication table: multiply each row number by each column number.
matrix = [[r * c for c in range(1, 4)] for r in range(1, 4)]
# The table has rows inside a larger list. Take each number from each row
# and place them in one list: [1, 2, 3], [2, 4, 6], [3, 6, 9]
# becomes [1, 2, 3, 2, 4, 6, 3, 6, 9].
# "for row in matrix" visits each inner list, one row at a time.
# "for x in row" visits every number in that row, and adds it to the new list.
flat = [x for row in matrix for x in row]

# Show the answers. labels[:4] means show only the first four labels.
print("squares:", squares)
print("evens:", evens)
print("labels:", labels[:4])
print("cubes:", cubes)
print("lengths:", sorted(lengths))
print("matrix:", matrix)
print("flat:", flat)

# Comprehensions used in this program, written without their surrounding brackets:
# n**2 for n in nums  # Square each number in nums.
# n for n in nums if n % 2 == 0  # Keep only numbers divisible by 2.
# "even" if n % 2 == 0 else "odd" for n in nums  # Label each number even or odd.
# n: n**3 for n in nums if n <= 5  # Pair each number up to 5 with its cube.
# len(w) for w in ["apple", "fig", "kiwi", "plum", "pear"]  # Get each word's length.
# r * c for c in range(1, 4)  # Multiply row number r by each column number c.
# [r * c for c in range(1, 4)] for r in range(1, 4)  # Make one multiplication row for each r.
# x for row in matrix for x in row  # Take every number from each row in matrix.
