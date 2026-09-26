''' Write a python program to translate a message into secret code language. Use the rules below to translate normal English into secret code language'''

# coding:
# if the word contain atleast 3 charachters, remove the first letter and append it at the end 
# now append the three random characters at the starting and the end
#else:
    # simply reverse the string


# Decoding:
# if the word contains less than 3 charachters, reverse iter
# else:
#     remove 3 random characters from start and end. Now the last letter  and append it to the beginning

# now this one the way sir did this one I also had solve this one but that was effective for a single words

'''Talha sir first splitten the text split(split when you find what i write here)[it returns a list] than use for loop to got to every word/item of the list words which was formed bu spliting string looks at each word if below len 3 reverse it [::-1] -1 is step (cofusion how it workd completely) the simple concatination then appending the comming words back into another list then finally converitng back that list to back string and thus printing''' 
st = input("Enter message")
words = st.split(" ") # didn't use
# print('used split key word',words)  # this one was just to see how it works
coding = input("1 = coding and 2 = decoding")
coding = True if (coding == "1" ) else False # wrong one-> coding = False
if(coding):
    nwords=[] # why got the list 
    for word in words:
        if(len(word)>=3):
            r1 = "wds"
            r2 = "des"
            stnew = r1 + word[1:] + word[0] + r2
            nwords.append(stnew)
        else:
            otherC = word[::-1]
            nwords.append(otherC)
    print(nwords)
    print(' '.join(nwords))
else:
    nwords = []
    for word in words:
        if(len(word)>=3):
            stnew = word[3:-3]
            stnew =stnew[-1] + stnew[:-1] 
            nwords.append(stnew)
        else:
            nwords.append(word[::-1])
    print(" ".join(nwords))