                                          ###### Dictionary data types

# Dictionary data type is unordered, mutable, Hetrogenious collection of elements where there are {keys:values} and keys are immutable while values can be mutable. Keys must be different but values can be same

dic = {'first_name' : 'rushi',
     'std' : 33}
print(dic)
print(id(dic))

# TO edit dictionary

dic['last_name'] = 'Gaware'

print(dic)
print(id(dic))

# Q. Create one dictionary with all your academics records. (10th to P.G)

a = eval(input("Enter your 10th marks : "))
b = eval(input("Enter your 12th marks : "))
c = eval(input("Enter your BSC marks : "))
d = eval(input("Enter your PGDM marks : "))

marks = {'10th' : a, '12th' : b , 'Bsc' : c, 'PGDM' : d} 

inf = {'Rushikesh' : marks}

print(inf)


########################### Operator's #############

# A. Arithematic Operators

num1 = 11
num2 = 2

sum = num1 + num2
sub = num1 - num2
div = num1/num2
floordiv = num1//num2
modu = num1%num2
multi = num1 * num2

print(sum)
print(sub)
print(div)
print(floordiv)
print(modu)
print(multi, end = '\n\n')

# B. Comparision Operators

print(num1 < num2)
print(num1 > num2)
print(num1 <= num2)
print(num1 >= num2)
print(num1 == num2)
print(num1 != num2, end = '\n\n')

# C. Assignment Operators

num1 += 2
num2 -= 4
num1 %= 3
num2 *= 3
num1 /= 5 
num2 //= 5

# D. Logical Operators

x = 10
z = 20

print(x<z and z>x)
print(x==z or z!=x)
print(not(x>9))
