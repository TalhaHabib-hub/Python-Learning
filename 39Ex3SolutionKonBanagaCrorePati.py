# This below is what I did by thinking what I fealeed and showed what I had learned.
# money2 = 0
# money1 = 0
# money3 = 0
# listofMoney = [10000,20000,40000,80000,160000,320000,640000,5400000,10000000]
# for i in range (len(listofMoney)):
    
#     print(f"Question for Rs.{listofMoney[i]}")
#     print(f'a. Python                   b. JavaScript')
#     print(f'c. Php                      d. C++')
#     answer = int(input("Enter your answer (1-4)"))
#     if answer == 4:
#         money2 = listofMoney[i]
#         if i == 3:
#             money1 = money2
#         elif i == 6:
#             money3 = money2
#     else: 
#         print("wrong answere!")
#         if i >= 3 and i< 6:
#             if i==3:
#                 print(f"you won Rs.{money1}. Luckily got to the 1st checkpoint!")
#             else:
#                 print(f"you won {money1} because You became unable to safe your balance after Rs.{listofMoney[3]} at least you had to crose till at RS.{listofMoney[6]}")
#             break
#         elif i >= 6 and i<len(listofMoney):
#             if i==6:
#                 print(f"you won {money2}. Luckily got to the 2nd checkpoint!")
#             else:
#                 print(f"you won {money2} because You became unable to safe your balance after Rs.{listofMoney[6]} you had to crose till at Rs.{listofMoney[-1]} for getting all the money!")
#             break
#         else:
#             print(f"You won Rs.{0} because You became unable to take your self to safe your balance atleast you need to had crossed Rs.{listofMoney[3]}" )
#             break
#     print(f"you have won Rs.{money2}")
#     if money2 == listofMoney[-1]:
#         print("Congragulations you got the top one!")
#     print("\n")


'''below from here is what Sir did'''
questions =[["which language was to create fb?", "python","French","javaScript","Php","None",4],
            ["which language was to create amazon?", "python","French","javaScript","Php","None",3],
            ["which language was to create whatsapp?", "python","French","javaScript","Php","None",3],
            ["which language was to create twittor?", "python","French","javaScript","Php","None",2],
            ["which language was to create python?", "python","French","javaScript","Php","None",3],
            ["which language was to create macos?", "python","French","javaScript","Php","None",4],
            ["which language was to create linkdin?", "python","French","javaScript","Php","None",4],
            ["which language was to create django?", "python","French","javaScript","Php","None",3],
            ["which language was to create flutter?", "python","French","javaScript","Php","None",2],
            ["which language was to create cobol?", "python","French","javaScript","Php","None",3]]
    

levels = [1000,2000,3000,5000,10000,20000,40000,80000,160000,320000]

money = 0
for i in range(len(questions)):
    question = questions[i]
    print(questions[i][0])
    print(f"Question for Rs. {levels[i]}")
    print(f"a. {question[1]}      b. {question[2]}")
    print(f"c. {question[3]}  d. {question[4]}")
    reply = int(input("Enter your answere (1-4)"))
    if(reply==question[-1]):
        print(f"correct answer, you have won Rs.{levels[i]}")
        if(i==4):
            money == 10000
        elif(i==9):
            money = 320000
        elif(i == 14):
            money = 10000000
    else:
        print("wrong answer!")
        break
    print("\n")    
print("your take home mony is",money)


# Talha I also had written another some sort of good one chech that in for Git folder let me put that here wait.....
'''
listsOfQuestions = [["Which of the following is a scalar quantity?", "Density","Displacement","Torque","Weight",1],["Which of the following is a the only vector quantity?", "Temperature","Energy","Power","Momentum",4],["Which of the following lists of physical quantities consists only of vectors?", "Timpe,Temperature,Velocity","Force,Volume,Momentum","Velocity,acceleration,mass","Force,Acceleartion,Velocity",4],["The angle between rectangular components along x-axis is?", "0'","60'","90;","120'",3],["A force of 10N is acting along y-axis. its component along x-axis is?", "10N","20N","100N","Zero N",4],["The vector product of two non zero vectors is zero, when?", "They are parallel to each other","They are perpendicular to each other","They are equal vectors","They are inclined at angle of 60'",1],["Identify the vector quantity?", "Heat","Angular momentum","Time","work",2],["Which of the following is a scalar quantity?", "Magnetic momentum","Acceleration due to gravity","Electric field","Electrostatic potential",4],["The resultant of two equal forces is double of either of the force. The angle between them is?", "0'","60'","90","120",1],["The resultant of two equal forces is double of either of the force. The angle between them is?", "0'","60'","90","120",1]]

markstore = 0
reward = [10,20,30,40,50,60,70,80,90,100]
treward = 0
for i in range(0,len(listsOfQuestions)):
    print(f"Q.{i+1}")
    print(listsOfQuestions[i][0])
    print(f"1.{listsOfQuestions[i][1]}")
    print(f"2.{listsOfQuestions[i][2]}")
    print(f"3.{listsOfQuestions[i][3]}")
    print(f"4.{listsOfQuestions[i][4]}")
    ans = int(input("choose (1-4)"))
    if ans ==listsOfQuestions[i][-1]:
        print("Correct")
        markstore = markstore + 10
        print("Your points",markstore,"/",(i+1)*10) 
    else:
        
        
        print("Wrong!---------> correct:",end=""),print(listsOfQuestions[i][listsOfQuestions[i][-1]]),print("Your points",markstore,"/",(i+1)*10)
    print("")

print("you got",markstore,"/",100)
''' # here it is  I loved the project... my first project for pushing to github