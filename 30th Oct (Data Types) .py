
################################# DATA TYPES ##########################################

# Integer data type only stores single numeric value (not decimal)

print('*' * 100)

a = 10
print(a)
print(type(a))

# Float data type only stores single decimal value

print('*' * 100 ,)

b = 22.33
print(b)
print(type(b))

# Boolean data type is a conditional data type

print('*'* 100)

x = 10
y = 20
z = x < y
print(z)
print(type(z))

# Complex number has two variants Real and imaginary (a + bj)
# a = real part (only integer(binary,hexa,octal,decimal))
# b = Imaginary part (Only decimal or float)

print('*' * 100)

com = 10 + 20j
print (com) 
print(type(com),end = '\n\n')

com1 = 0b1010 + 22.34j
print(com1)
print(type(com1),end = '\n\n')

com2 = 22.33 + 44j
print(com2)
print(type(com2),end = '\n\n')

com3 = 0xAFEB + 22.45j
print(com3)
print(type(com3),end = '\n\n')

com4 = 0o7434 + 55j
print(com4)
print(type(com4))
      
# String data type only store one word or one sentence in a inverted comma

print('*' * 100)

str = 'rushi'
print(str)
print(type(str))


# List data type is ordered, Mutable, Hetrogenious collection of elements where duplicates are allowed values are stored in closed brackets and seperated by comma

print('*' * 100)

c = [10,22.22,'yo',44,22,45]
print(c)

## Add data in list

c.append('hello')       
print(c)
print(type(c))

## Remove data from list

c.remove(10)
print(c)

# Tuple data type is ordered, Immutable, Hetrogenious collection of elements where duplicates are allowed values are stored in paranthesis brackets and seperated by comma

print('*' * 100)

d = (10,'helo',33.44)
print(d)
print(type(d))

# Dictionary data type is unordered, Mutable, Hetrogenious collection of elements where there are {keys:values} and keys are immutable while values can be mutable. Keys must be different but values can be same

print('*' * 100)

e = {'name' : 'rushi',
     'std' : 33}
print(e)

# The new data is added in dictionary as it is mutable

e['roll'] = 99
print(e)
print(type(e))

# Set is un-ordered, Mutable, Hetrogenious collection of elements where insertion order is unpreserved and duplicates are not allowed

print('*' * 100)

f = set ('helo')
print(f)
print(type(f))

## Add data in Set

f.add('bye')
print(f)

## Remove data from set

f.remove('bye')
print(f)
