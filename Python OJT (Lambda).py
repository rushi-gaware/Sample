# Variable using Lambda -

loop = lambda a,b,c,d : d if a > b else c
print(loop(10,11,'yes','no'))

# Function using lambda -

# A. Normal way

print('*' * 100,end = "\n\n")

def display (a) :
    print(a)
    
def add (a,b) :
    return a + b
    
display(add(10,20))

# B. Using Lambda

def calculate (a) :
    return lambda : a*a

y = calculate (10)
z = y()
print(z)

  