import os

# os.rename('clutter/file.txt','clutter/6.txt') # it worked
files = os.listdir('clutter')
i = 33
for file in files:
    
    if file.endswith('.png'):
        print(file)
        os.rename(f'clutter/{file}',f'clutter/{i}.png')
        i += 1