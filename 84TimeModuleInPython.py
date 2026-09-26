import time
'''
def usingWhile():
    i = 0
    while i < 50000:
        print(i)
        i += 1

def usingFor():
    for i in range(50000):
        print(i)

init = time.time()
usingWhile()
whili = time.time() - init

secInit = time.time()
usingFor()
forli = time.time()- secInit

print(f'while took {whili}sec')
print(f'for took {forli}sec')
'''

print('Talha, You will go to_________wait for 3 sec________')
time.sleep(3)
print("Love ---> Madinah")
print('')
t = time.localtime()
formatted_time = time.strftime('%I:%M %p')
print(' ',formatted_time)
formatted_time = time.strftime('%m/%d/%Y')
print(formatted_time)