def welcome():
    print("Hey you are welcome from Talha")

# so i think Talha you came here after reading what you wrote in 45th file so to solve the discussed issue we do this 

print(__name__) # the name of this file is "__main__" from the other file like 45th file it will print the name of the module but here it is printing the __main__ so it mean again i am saying that the __name__ for other file the where this file is imported will be the name of the file so inthat case the below condition will be false and the welcome() willnot be executed for them but here __name__ is assigned as __main__ so will only be executed for here
if __name__ == "__main__":  # this is just telling that automatically get executed only here when called in this main file so it will not be executed on its own in the main file
# here earlier the lest time i used the main word it was just for the this file the curent file in which you are is considered the mian file
    welcome()