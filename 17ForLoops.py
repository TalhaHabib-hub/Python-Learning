'''
Sometimes a programmer wants to execute a group of statments a certain numbers of times. This can be done using loops. Based on this loops are further classified into following types; for loop, while loop, nested loops.
'''
# iterating over a string
name = "Talha"
for i in name:
    print(i, end="")
    if i == "h":
        print(" This is awesome")
print("")
colors = ["Red","blue","Yelow"]
for color in colors:
    print(color)
    for char in color:
        print(char)

#range()
for i in range(2,21,4):
    print(i,end=" ")