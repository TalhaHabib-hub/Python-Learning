i = 4
rows = i
cols = i
matrix=[]
for i in range(rows):
    row=[]
    for c in range(cols):
        row.append(0)
    matrix.append(row)
    
for row in matrix:
    print(' '.join(map(str, row)))

for level in range(1, rows + 1):
    print(' ' * (rows - level)  + '*' * (2 * level - 1))

nums =[1,2,3,4]
squares =list(map(lambda x: x*x, nums))

print(squares)