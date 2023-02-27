################## Flow control Statement #################

# 1. Conditional Statement ( if, if-else, if-elif-else )

viru = 22
shiv = 22

if viru>shiv:
    print("Viru is older than shiv")
    
elif viru<shiv:
    print("Shiv elder than Viru")

else:
    print("Both are of same age")
    
print('-' * 130)

l = [20,55,-55,77,88,99,-21,-54,-654,-87,-54]

nega = []
posi = []
even = []
odd  = []

for i in l:
    if i < 0:
        nega.append(i)
    elif i > 0:
        posi.append(i)
    elif i%2 == 0:
        even.append(i)
    elif i%2 == 1:
        odd.append(i)
    else:
        pass

print(nega)
print(posi)
print(even)
print(odd)

st = 'facebook'
le = len(st)
ra = range(le)

for j in ra:
    print(st[j] * (j+1))

print('-' * 130)

a = 'instagram'
l = len(a)
r = range (l)

for i in r:
    print(a[i] * (9-i))