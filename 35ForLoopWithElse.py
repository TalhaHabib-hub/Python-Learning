'''---------------------Python - else in Loop-------------------------------'''
# As you have learned before, the else clause is used along with the if statment.
# Python allows the else keyword to be used with the for and while loops too. The else block appears after the body of the loop. The statements in the else block will be executed after all iterations are completed. The program exits the loop only after the else block is executed.
for i in range(5):
    print(i)
    # if i == 4:
    #     break
else:
    print("Sorry")