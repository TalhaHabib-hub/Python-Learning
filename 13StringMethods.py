# string is immutable
a = "!!Harry!!!!!!!"
print(len(a))
print(a.upper())
print(a.lower())
# the rstrip removes any trailing character
print(a.rstrip("!"))
print(a.rstrip("r"))

#replace()
# the replace() method replaces 'all occurances' of a string with another string.
print(a.replace("Ha","Ty"))
naam = "Talha, Talha, Saqib, Jibran, Talha,TAlha"
print(naam.replace("Talha","Son of Habib"))


# split method splits the given string at the specified instance and returns the seperated string as list items

kaam = "Hall chalana Parhna"
print(kaam.split("a"))
print(kaam.split(" "))

# the capitalize method turns only the first character of the string to uppercase and the rest other characters of the string are turned to lowercase. The string has no effects if the first charcter is already uppercase.
boldheading = 'introductiOn to pYthon i am ..'
print(boldheading.capitalize())

# the center method aligns the string to the center as per the parameters given by the user
air = "pakistan Air Force"
print(air.center(54),end="<- ")
print("dono side dakh")
print(len(air))
print(len(air.center(54)))
#so this mean if i have a variable a = "Talha" and then if write print(a.center(42)) so python will add space equally at the start and also at the end and will make the length 42
print("Talha".center(9,"*"))
# count()
# The count() method returns the number of times the given value has occured within the given string

er = "Talha habib hazir ha"
print(er.count("ha"))

#also we have starts with
# the endswith() method checks if the string ends with a given value. if yes the return True. else False
print(er.endswith("ha"))
print("dk",er.startswith("Ta"))
# We can even also check for a value in-between the string by providing start and end index position
# like
print(er.endswith("a", 1, 5)) # ->'lha'

#find()
# The find() method searches for the 'first' occurance of the given value and returns the 'index' where it is present. If given value is absent from the string then return -1
print(er.find("ha"))
print(er.find("ahee"))

#index()
# same as find but if the value not found it will rase error

#isalnum()
# The isalnum() method returns True only if the entire string only consists of A-Z, a-z. If andy other character s or punctuation are present then it will returns Flase

tr = "owihweQ"
ur = "owihwe2442"
print(tr.isalnum()) #True

#isalnum()
#The is isalnum() method returns True only if the entire string only consists of A-Z, a-z, 0-9. If andy other character s or punctuation are present then it will returns Flase
print(ur.isalnum()) # True

#islower and isupper
# the islower() method returns True if all the characters in the string are lower case, else it returns False
print(tr.islower()) # False

#isprintable()
# THE isprintable() methods returns true if all the values within the given string are printable, if not (\n is not printable), then return false
print(tr.isprintable()) # True

#ispace()
#isspace() method returns True only and only if the string contains atleast one  white space.
print(tr.isspace()) # False


#istitle()
# the istitle() returns True only if the first letter of each word of the string is capitalized. else it returns False.
tt = "Talha Habib Dreamer"
print(tt.istitle()) # True

#swapcase()
# the swapcase() changes the character casing of the string. uppercase are converted into lower case and lower case are converted into upper
gh = "talha"
print(gh.swapcase())
print((gh.swapcase()).swapcase())
print("Talha".swapcase()) #->tALHA
# this below one will convert the string into title
# title mean capitalizing each letter of the word within the string
gh = "talha habib khan will do it"
print(gh.title()) # ->Talha Habib Khan Will Do It
