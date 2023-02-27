# 3. Default Argument - 

def e_mail (fname,lname,cname = "tcs") :
    print(fname+"_"+lname+"@"+cname+".com")
    
first_name = input("Enter the first name : ")
last_name = input("Enter the last name : ")

a = e_mail (first_name,last_name,"purnartha")

#. 4. Arbirary Argument - 
# i).  Positional Arbitary Args (*args)
# ii). Keyword Arbitary Args    (**kwargs)

# i). If we don't know how much input we will be getting then we use *args as argument. We will get in    the form of tupple.

def inp (*args) :
    print(args)
    print(type(args))
    
inp (10,50,30,50,78,965,6565,56,5,54654,654864,8789,'helo')

def add_unknown (*args) :
    result = 0
    for i in range(len(args)) :
        result += args[i]
    print(result)

add_unknown(10,20,30,50,78,965,6565,56,5,54654,654864,8789)

# ii). Arguments are passed in the form of key:value 

def add_unknown1 (**kwargs) :
    print(kwargs)
    print(type(kwargs))
    
add_unknown1 (num1 = 10,num2 = 44,num3 = 22, num4 = 578)


def add_unknown2 (**kwargs) :
    for k,v in kwargs.items():
        print(k,'------>',v)
 
    
add_unknown2 (num1 = 10,num2 = 44,num3 = 22, num4 = 578)




# ________________________________________________________________________________________________________

# NOTE = (*)  Single star means it will give output in the tuple form
#      = (**) Double star means it will give output in the dictionary form

