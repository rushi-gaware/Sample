# Types of Programming - 

# 1. Sequential Programming
# 2. Functional Programming 
# 3. OOPS


# 1. Sequential - 

# 2. Functional Programming - 

# Q. Add two numbers
'''
print("First this will be executed \n\n")

def add ():
    print("Thirdly this will execute, we are inside of function \n\n")
    num1 = eval(input("Enter first the number : "))
    num2 = eval(input("Enter second the number : "))
    total = num1 + num2
    print(f"The sum of {num1} and {num2} is {total} \n\n")
    
print("Secondly this will be executed, here function is called \n\n")
add()
print("This is the last statament")

def email ():
    f_name = input("Enter your first name : ")
    l_name = input("Enter your first name : ")
    c_name = input("ENter your company's name : ")
    e_mail = (f"{f_name}.{l_name}@{c_name}.com")
    print(e_mail)

while True:
    email()
    
    '''
    
print("We are in GLobal Scope")

def multi():
    print("We are in local scope")
    y = 40
    sum = (x + y)
    min = (x-y)
    print(sum)
    return min
x = 60
print("Before calling the function")
a = multi()
print(a)

