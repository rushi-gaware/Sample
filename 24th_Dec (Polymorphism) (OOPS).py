# 2. Polymorphism


# A.OverLoading -                                       B. Overriding -
#   i) . Variable Overloading                               i) . Variable Overriding
#  ii) . Method Overloading                                ii) . Method Overriding

# i). Variable Overloading -

# Multiple overloading can be done on num1 and num2

num1 = 10
num2 = 20

print (num1 + num2)
print (num1 - num2)
print (num1 * num2)

print()
print('-' * 150)
# ********************************************************************************************************

# We only define or create method like add,sub,mul to only user defined function

class Book :
    def __init__ (self,nm,clr,pg,pr) :
        self.name = nm
        self.color = clr
        self.page = pg
        self.price = pr
        print("\n\n"f"The name of the Book is {self.name}, color is {self.color} and pages are {self.page} is of price {self.price}",end = "\n\n")
        
    def __add__ (self,other) :
        return (self.page + other.page)
    
    def __sub__ (self,other) :
        return (self.price - other.price)
    
    def __mul__ (self,other) :
        return (self.price * other.price)
        

b1 = Book ("GOT","Black",500,1100)

b2 = Book ("How to Make Money","Red-White",156,800)

print (b1 + b2) # This will give pages addition

print(b1 - b2) # This will give prices subraction

print(b1 * b1) # THis will give product of 2 book prices


# ii). Method Overloading - Basically Method overloading is not possible in python because it is dynamically typed.