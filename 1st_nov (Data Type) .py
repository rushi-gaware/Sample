# Range data type returns the whole number to the infinity but not float number (0 to +number) or (-number to 0)

a =  range(10)
for i in a:
    print (i)

# Q. In the word "INSTAGRAM" print word 'G' with its index value?

s = 'Instagram'
l = len(s)
r = range (l)

for j in r:
    if s[j] == 'G':
        print(s[j] ,'Its index value is :' , j)
        
# Q . Print the table of any numeric value

num = eval(input("Enter the number you want to create table of : "))
r = range (1,11,1)

for i in r:
    print(num , '*' , i, '=', i*num)
        
