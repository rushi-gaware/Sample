class Laptop :
    Type = "handy"
    def __init__ (self,nm,feat,clr) :
        self.name = nm
        self.feature = feat
        self.color = clr
    
    @classmethod
    def types (cls) :
        print (f"Laptop type is {cls.Type}")
        
    @staticmethod
    def add_two (a,b) :
        print(f"Addition of {a} and {b} is {a+b}")
    
l1 = Laptop ('HP',"144 Hz","black")

l1.types ()
l1.add_two(10,11)