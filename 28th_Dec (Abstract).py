# 3.Abstract -

from abc import ABC,abstractmethod

class RBI (ABC) :
    
    @abstractmethod
    def cust_care (self) :
        pass
        
class SBI (RBI) :
    
    def __init__ (self,acno,bal,ty) :
        self.account_no = acno
        self.balance = bal
        self.acc_type = ty
        
    def type (self) :
        print(f"Your account type is {self.acc_type}")
        
    def cust_care (self):                                               # Here cust_care method is cumpolsary to be called as it belong to abstracr class ro else code won't get execute
        print("If you have any querry contact us on : 8657730558")
    
c1 = SBI (8989,5656,"Saving")
c1.type ()
c1.cust_care ()

class HDFC (RBI) :
    def __init__ (self,acno,bal,ty) :
        self.account_no = acno
        self.balance = bal
        self.acc_type = ty
        
    def type (self) :
        print(f"Your account type is {self.acc_type}")
        
    def cust_care (self) :
        print("DO contact us on 9422792098 in case of any querries")
        
c1 = HDFC (11665599,8000000,"Current")
c1.type ()
c1.cust_care ()

