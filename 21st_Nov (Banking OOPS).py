class Bank :
    bank_name = "SBI"
    def __init__ (self,nm,act_type,acno,bal) :
        self.name = nm
        self.account_type = act_type
        self.account_No = acno
        self.balanced = bal
    
    def details (self) :
        print("\n\n" f"Account Number is {self.account_No} with the {self.account_type} in the name of {self.name} and has balance of {self.balanced}. ",end = "\n\n")
        
    def balance (self) :
        while True :
            print('''
                  
                  1. Do you want to Withdraw
                  2. Do you want to Deposit
                  
                  ''')
            ch = eval(input("Enter your Input : "))
            
            
            if ch == 1 :
                print()
                withdraw = eval(input("Enter the amount you want to Withdraw : "))
                if withdraw > self.balanced :
                    print("\n\n" "Sorry Insufficient Balance.............", end = "\n\n")
                else :
                    self.balanced -= withdraw
                    print("\n\n" f"Your remaining balance is : {self.balanced}", end = "\n\n")
   
                break
                                  
            if ch == 2 :
                print()
                deposit = eval(input("Enter the ampunt you want to deposit : "))
                self.balanced += deposit
                print("\n\n" f"Your new Balance is : {self.balanced}",end = "\n\n")
                break
                
            else :
                print("\n\n" "Please Select Appropriate Input....", end = "\n\n")
            
            break
        
        
        
      
a1 = "Saving"
a2 = "Current"  

b1 = Bank ("Rushi",a1,899889899,1000)
b1.details ()

print(b1.bank_name)