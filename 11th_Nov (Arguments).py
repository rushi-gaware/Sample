# 1. Positional Argument - 

def add (x,y):
    print(x + y)
    
num1 = int(input("Enter you 1st num : "))
num2 = int(input("Enter you 2nd num : "))

sum = add (num1,num2)


# 2. Keyword Arguments - 

def mul (p,q) :
    print(p * q)

num3 = int(input("Enter you 1st num : "))
num4 = int(input("Enter you 2nd num : "))

prod = mul (p = num3,q = num4)