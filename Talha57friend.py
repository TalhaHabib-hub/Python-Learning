def largest_in_Tuple(*l):
    large = 0
    for i in l:
        if i > large :
            large = i
    return large

print(largest_in_Tuple(2,9,34,5,8))
