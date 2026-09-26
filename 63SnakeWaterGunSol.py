
import random

def check(comp, user):
    if comp == user:
        return 0
    if comp == 0 and user ==1:
        return -1
    if comp == 1 and user ==2:
        return -1
    if comp == 2 and user ==0:
        return -1
    return 1

print('''_________Rules_________
Snake beats water
      Gun beats snake
             Water beats Gun''')
user =int(input("Enter 0 for Snake, 1 for water, and 2 for gun "))
comp = random.randint(0,2)
ya =  {0:"Snake",1:"Water",2:"Gun"}




print("you =",ya[user],"| computer =",ya[comp])
score = check(comp, user)
if(score == 0):
    print("its draw")
elif score == 1:
    print("You Lose")
else:
    print("you won")