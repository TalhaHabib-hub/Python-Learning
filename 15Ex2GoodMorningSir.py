import time
# strftime() is a function that gives us hours, minutes and seconds in vscode it is giving the time from my device
timestamp = time.strftime('%H:%M:%S') #for 24 format
# print(time.strftime('%I:%M %p')) #for 12 format
print("The actual time :",timestamp)
timestamp = int(time.strftime('%H'))
print("hours  ",timestamp)
timestamp = time.strftime('%M')
print("minutes",timestamp)
timestamp = time.strftime('%S')
print("seconds",timestamp)
#https://docs.python.org/3/library/time.html#time.strftime
'''
Morning   — 12:00 AM to 12:00 PM (midnight to noon)
Afternoon — 12:00 PM to 5:00  PM (noon to 5pm)
Evening   — 5:00  PM to 9:00  PM
Night     — 9:00  PM to 12:00 AM


'''
# this below one is my code

# if (int(time.strftime('%H'))>=1 and int(time.strftime('%H'))<12):
#     print("Good Morning Talha")
# elif (int(time.strftime('%H'))>=12 and int(time.strftime('%H'))<17):
#     print("Good Afternoon Talha")
# elif (int(time.strftime('%H'))>=17 and int(time.strftime('%H'))<22):
#     print("Good Evening Talha")
# else:
#     print("Good Night Talha")


# when AI cooks

hour = int(time.strftime('%H'))

if hour < 12:
    print("Good Morning Talha")
elif hour < 17:
    print("Good Afternoon Talha")
elif hour < 22:
    print("Good Evening Talha")
else:
    print("Good Night Talha")
    


'''
import time

print(time.strftime('%I:%M %p'))
-----> this code will give us the time in 12 format
'''
print(time.strftime('%I:%M %p'))

print('###########################################')


print(time.strftime('%I:%M %p'))    # 05:19 PM
print(time.strftime('%d %B %Y'))    # 27 May 2026
print(time.strftime('%d'))          # 27
print(time.strftime('%B'))          # May
print(time.strftime('%Y'))          # 2026 -> small y just 26
print(time.strftime('%A'))          # Wednesday


# the way "time.strftime('%A')" used can make you confuse you because we normally use the . for objects but time is module, so the key take away is it can be use for both objects and module and it just mean is go inside of it and do this for it
#############################################
'''

'''