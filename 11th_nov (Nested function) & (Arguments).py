
def outer_func():
    print("We are in outer function")
    
    def inner_func ():
        print("We are in inner function")
        
        def inner_func2 ():
            print("We are in inner function 2")
            
        return inner_func2 
    
    return inner_func    
            
a = outer_func ()                     # This contains inner function in it
b = a ()                              # This contains inner function 2 in it
b()                                   # All functions are called

# Recursive function - 

def fun () :
    i = 5
    return fun ()

fun()

