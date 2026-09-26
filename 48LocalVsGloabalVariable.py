# x = 3


# def hello():
#     x = 4 # without it 3 will be printe
#     y = 6
#     print("Local variable",x)
# print("Gloabal variable",x)
# hello()
# print("Gloabal variable",x)

# now sir is saying what should I do that after calling the function the gloabal will change
# for doing it use the global keyword
x = 3


def hello():
    global x # without it 3 will be printe // gloabal x = 4 incorrect
    x = 4
    y = 6
    print("Local variable",x)
print("Gloabal variable",x)
hello()
print("Gloabal variable",x)

# print(y) #NameError: name 'y' is not defined