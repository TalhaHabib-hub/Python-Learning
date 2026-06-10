# same same
for i in range(3):
    print(i)

i = 0
while(i<3):
    print(i)
    i+=1

# in some conditions it becomes more convinient then for loop like 
# if I want to ask the user to put the number unless he guess correctly for solving this problem we can use while but not for loop

i = int(input("Enter the number : "))
while i != 100:
    i = int(input("Enter the number : "))
    