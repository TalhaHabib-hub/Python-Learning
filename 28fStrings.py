# use for string formating
# befor fstring string formating was like this 
# In the strings if I had to add variables value i would do this as shown below but it isn't that much convinient because it will make confusion if our probram is big it becomes difficult for us to understand that where is this varible comes into the string to solve this issue and make our code readable we got our fstring property.so we go to line 15.
letter = "Hey! my name is {} and I am from {}"
country = "pakistan"
name = "Talha"
print('1.',letter.format(name, country))

# and if you are wanting that there order shouldn't matter then
letter = "Hey! my name is {1} and I am from {0}"
country = "pakistan"
name = "Talha"
print('2.',letter.format(country,name))

print(f"3. Hey! my name is {name} and I am from {country}")

# writing .2f // also Talha hi didn't putted the variable in line 19 he even made variable inside it
string = "The money in the store is {money:.2f}"#----->:.2f
print(string.format(money = 24.34453454)) # Talha do this if you want to take just till the two floating point decimal.
# writing .2f


# using fstring
money = 24.34453454
string = f"The money in the store is {money:.2f}"#----->:.2f
print(string) # Talha do this if you want to take just till the two floating point decimal.

'''{money:.2f}---printing this instead of the value so lets go '''
string = f"The money in the store is {{money:.2f}}"#----->:.2f
print(string) # Talha do this if you want to take just till the two floating point decimal.

