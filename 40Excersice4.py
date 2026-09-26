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

# word = "Talha"
# word2 = word[1:]
# print(word2)
# word3 = word2 + word[0]
# print(word3)
# word4 = 'ete'+word3+'wer'
# print(word4)

# word5 = word4[3:-3]
# print(word5)
# word6 = word5[:-1]
# print(word6)
# word7 =word5[-1] + word6 
# print(word7)

#coding
wordforSending = input("Enter the word.")
if len(wordforSending)<4:
    word  = ""
    for i in  range (len(wordforSending)-1,-1,-1):
        word = word + wordforSending[i]
    print('for your security it is send this way->',word)
else:
    word = wordforSending[1:] + wordforSending[0]
    word = 'ers' + word + 'cww'
    print("ready to send",word)

# decoding
wordrecived = input("put the word that is code according to the rule:")
if len(wordrecived)<4:
    word  = ""
    for i in  range (len(wordrecived)-1,-1,-1):
        word = word + wordrecived[i]
    print('This was the word ',word)
else:
    word = wordrecived[3:-3]
    word = word[-1]+word[0:len(word)-1]
    print("ready",word)