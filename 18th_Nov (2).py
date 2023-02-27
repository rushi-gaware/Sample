# Q. Arrange the list in ascending order without using sort function?

l = [36,45,2,7,33,1,9]

for i in range(len(l)) :
    min_val = min(l[i:])
    index_val = l.index(min_val)
    l[i],l[index_val] = l[index_val],l[i]
    
print(l)