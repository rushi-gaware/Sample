# Q. Arrange in ascending
'''
l = [11,44,3,2,77]

for i in range(len(l)):
    min_val = l[i]
    for j in range (i+1,len(l)) :
        if min_val > l[j] :
            min_val = l[j]
    min_index = l.index(min_val)
    l[i],l[min_index] = l[min_index], l[i]
        

print(l)'''

# Q. 

l = [22,6,33,9,66,4]