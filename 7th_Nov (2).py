# Q1. Print the list in ascending order :

# 1. Method 1 -

l = [10,11,8,7,6,2,7,22,77,5,11,33,88,99]

l.sort()
print(l)

# 2. Method 2 -

for i in range(len(l)) :
    min_value = min(l[i:])
    min_index = l.index(min_value)
    l[i],l[min_index] = l[min_index],l[i]
    
print(l)

######################################################################################################


# Q2. Print list in ascending order [33,675,5,1,33,77]

li = []

for j in range (len(li)) :
    m_val = min(li[j:])
    m_index = li.index(m_val)
    li[j],li[m_index] = li[m_index],li[j]
    
print(li)