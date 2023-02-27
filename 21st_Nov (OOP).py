class Student :
    def __init__ (self,nm,rn,su,mk):
        self.name = nm
        self.rollno = rn
        self.subject = su
        self.marks = mk
        
s1 = Student ('Rushi',1,'Maths',100)
print(f"Student name is {s1.name} his roll number is {s1.rollno} has subject {s1.subject} and got marks {s1.marks}")


#=========================================================================================================================


class Employee :
    def __init__ (self,nm,sal,dep,id,mob):
        self.name = nm
        self.salary = sal
        self.department = dep
        self.employee_id = id
        self.mobile = mob
        
    def get_info (self) :
        print('\n\n'f"Employee name is {self.name} his ID is {self.employee_id} of department {self.department} and has salary of {self.salary}")

        
e1 = Employee ('Rushi',950000,'Developer',100,8657730558)
e1.get_info ()

e2 = Employee ('Shreya',515000,"Finance",101,9422792098)
e2.get_info ()


#=========================================================================================================================


class Bank () :
    def __init__ (self,bn,acc,nm,bal,typ) :
        self.bank_name = bn
        self.account_no = acc
        self.name = nm
        self.balance = bal
        self.type = typ
        
    def cr_bal (self,bl) :
        if bl > 0 :
            self.balance += bl
            print('\n\n'f"Ammount {bl} has been credited successfully and your total balance is {self.balance}")
        else :
            print("Balance must be Positive")
        
    def db_bal (self,db) :
        if db >= self.balance :
            print("Insufficient Balance")
        else :
            self.balance -= db
            print(f"{db} has been debited from your account, your Balance is {self.balance}")
        
    def balance (self) :
        print('\n\n'f"Your Balance is {self.balance}")
        

b1 = Bank ('SBI',8999,'Rushi',10000,'Saving')
amt = eval(input("Enter the amount you want to deposit : "))
b1.cr_bal (amt)

b2 = Bank ('HDFC',999,'Shreya',15000,'Current')
ammt = eval(input("Enter the amount you want to Debit :"))
b2.db_bal (ammt)

#######################################################################################################################################

# __init__ = It is a constructor which is used for the creation of attributes such as (self.name, etc)

# (self) = Every object has 2 reference vairbale -
# i). Reference Variable - e1 .
# ii). self - self is the name of object which is used inside of the class and reference variable is used outside of the class.
                                           