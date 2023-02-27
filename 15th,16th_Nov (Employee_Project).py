
db = {100: {'Name' : 'Tom', 'Dept' : 'HR', 'Salary' : 25000, 'Empid' : 100},
      101: {'Name' : 'John', 'Dept' : 'Sales' ,'Salary' : 60000 , 'Empid' : 101},
      102: {'Name' : 'Shawn' , 'Dept' : 'Testing', 'Salary' : 70000, 'Empid' : 102},
      103: {'Name' : 'Kevin' , 'Dept' : 'Finance' , 'Salary' : 50000, 'Empid' : 103},
      104: {'Name' : 'Ben' , 'Dept' : 'Marketing' , 'Salary' : 65000, 'Empid' : 104},
      105: {'Name' : 'Justin', 'Dept' : 'Accounting' , 'Salary' : 80000, 'Empid' : 105},
      106: {'Name' : 'Smith' , 'Dept' : 'Analyst', 'Salary' : 90000, 'Empid' : 106}  
     }

def dashboard ():
    print('-' * 33,"Welcome to Employee Management System",'-' * 30, end = '\n')
    
    print('''
          
                                      1. Add Employee Name
                                      2. Display employee Data
                                      3. Edit Employee Details
                                      4. Delete Employee Details
                                      5. Search Employee by Department
          ''')

    print('-' * 100)

def add ():
    add_eid = int(input("Enter Employee ID : "))
    add_name = input("Enter Employee name : ")
    add_dept = input("Enter Employee Department : ")
    add_sal = int(input("Enter Employee Salary : "))
    
    chotu_dict = {}
    
    chotu_dict['Name']   = add_name
    chotu_dict['Dept']   = add_dept
    chotu_dict['Salary'] = add_sal
    chotu_dict['Empid']  = add_eid
    
    db[add_eid] = chotu_dict
    
    print(f"You have successfully added {add_name} into database",end = '\n\n')
    
def display ():
    
    if len (db) == 0:
        print("Please add some data....")
        
    else: 
        print('-' * 100)
        print ("| {eid:^20} | {ename:^20} | {empdep:^20} | {empsal:^20} |".format(eid = 'Employee Id',ename = 'Employee Name',empdep = 'Employee Department',empsal = 'Employee Salary'))
        
        for i in db.values():
            print('-' * 100)
            print ("| {id:^20} | {nm:^20} | {dep:^20} | {sa:^20} |".format(id = i['Empid'] , nm = i['Name'], dep = i['Dept'], sa = i['Salary']))
            
        print('-' * 100)    
            
def delete () :
    if len(db) == 0:
        print("Please add some data.....")
    
    else :
        id = eval(input("Please enter employee ID : "))
        if id in db:
            del db[id]
            print("You have successfully deleted employee ID")
        else : 
            print("No ID found in the database.....")
            
def edit () :
    if len(db) != 0:
        id = eval(input("Enter Employee ID : "))
        if id in db :
            edit_name = input("Enter Updated Employee name : ")
            edit_dept = input("Enter Updated Employee Department : ")
            edit_sal = int(input("Enter Updated Employee Salary : "))
            
            db[id]['Name']  = edit_name 
            db[id]['Dept']  = edit_dept
            db[id]['Salary']  = edit_sal
            
            print(f"You have successfull edited the Employee Details of ID {db}")
            
            
while True:
    
    dashboard ()
    
    choice = int(input("Enter your choice : "))
    
    if choice == 1:
        add ()

    elif choice == 2:
        display ()
        
    elif choice == 3:
        edit ()
        
    elif choice == 4:
        delete ()
        
    else :
        print("Invalid input select Appropriate choice.....")
        
    ch = input("Do you want to continue (y/n) : ").lower()
    
    if ch != 'y':
        print("OK..... Thank You...")
        break