class Employee :
    
    company_name = "TCS"
    
    def __init__ (self,nm,sal,dept) :
        self.name = nm
        self.salary = sal
        self.department = dept
        
    def info (self) :
        print("\n\n"f"Employee name is {self.name} his department is {self.department} and has a salary of {self.salary}") 
        
    @classmethod
    def depart (cls) :
        Employee.company_name = "Infosys"
        print(f"This is new department {Employee.company_name}",end = "\n\n")
        
E1 = Employee ("Rushi",5000,"Finance")
E1.info ()
E1.depart ()

E2 = Employee ("Shreya",80000,"IT")
E2.info ()
E2.depart ()

Emp_list = []
Emp_list.append (E1)
Emp_list.append (E2)

for i in range(len(Emp_list)) : 
    print("Employee name is {n} and Salary is {s}".format(n = Emp_list[i].name , s = Emp_list[i].salary),end = "\n\n")