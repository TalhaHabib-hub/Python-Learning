import time
t = int(time.strftime('%H'))
print(t)
if t >= 0 and t < 12:
    print('Good Morning Sir!')
elif t>=12 and t < 17.8:
    print('Good Afternoon Sir!')
else:
    print('Good Night Sir!')
