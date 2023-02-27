db = {100: {'Name' : 'Tom', 'Dept' : 'HR', 'Salary' : 25000, 'Empid' : 100},
      101: {'Name' : 'John', 'Dept' : 'Sales' ,'Salary' : 60000 , 'Empid' : 101},
      102: {'Name' : 'Shawn' , 'Dept' : 'Testing', 'Salary' : 70000, 'Empid' : 102},
      103: {'Name' : 'Kevin' , 'Dept' : 'Finance' , 'Salary' : 50000, 'Empid' : 103},
      104: {'Name' : 'Ben' , 'Dept' : 'Marketing' , 'Salary' : 65000, 'Empid' : 104},
      105: {'Name' : 'Justin', 'Dept' : 'Accounting' , 'Salary' : 80000, 'Empid' : 105},
      106: {'Name' : 'Smith' , 'Dept' : 'Analyst', 'Salary' : 90000, 'Empid' : 106}  
     }

def dashboard () :
    
    print('-' * 33,"Welcome to Employee Management System",'-' * 30, end = '\n')
        
    print('''
              
                                          1. Add Employee Name
                                          2. Display employee Data
                                          3. Edit Employee Details
                                          4. Delete Employee Details
                                          5. Search Employee by Department
              ''')
    
    print('-' * 100)

def length ():
    if len(db) != 0:
        pass
    else :
        print("Your database is empty, add some data......")


def add () :
    
    length()
    
    add_ID = eval(input("Enter the Employee ID : "))
    add_Name = input("Enter the Employee Name : ")
    add_Dept = input("Enter the Employee Department : ")
    add_Salary = eval(input("Enter the Employee Salary : "))
    
    dic = {}
    
    dic['Name'] = add_Name
    dic['Empid'] = add_ID
    dic['Dept'] = add_Dept
    dic['Salary'] = add_Salary
    
    db[add_ID] = dic
    
    print(f"You have successfully added {add_Name} in the database")
    
    
def display ():
    
    print('-' * 100)
    
    print("{id:^20} {nm:^20} {de:^20} {sal:^20}".format (id = 'Employee ID', nm = 'Employee Name', de = 'Employee Dept', sal = 'Employee Salary'))
    
    print('-'* 100)
    
    for i in db.values ():
        print("{e_id:^20} {e_nm:^20} {e_dep:^20} {e_sal:^20}".format(e_id = i['Empid'], e_nm = i['Name'], e_dep = i['Dept'], e_sal = i['Salary']),end = '\n\n')
        print('-'*100)
        
        
def edit ():
    length ()        
    
    print( '''What would you like to edit...
                      
                      1. Employee Name
                      2. Employee Department
                      3. Employee Salary
        
    ''') 
    
    choic = eval(input("Select the input from : "))
    
    print()
    
    if choic == 1:
        id = eval(input("Enter Employee ID to edit the Name: "))
        print()
        
        if id in db:
            edit_name = input ("Please Enter the Edited Employee Name : ")
            print()
            db[id]['Name'] = edit_name
            print(f"You have successfully added {edit_name} in the Data list...")
            
        else :
            print("No Record Found....Please Enter Valid ID....")
    
    if choic == 2:
        
        id = eval(input("Enter Employee ID to edit Department : "))
        print()
        
        if id in db:
            edit_dep = input("Enter the Department name you want to update : ")
            print()
            db[id]['Dept'] = edit_dep
            print(f"You have successfully edit the Department to {edit_dep}")
    
    if choic == 3:
        id = eval(input("Enter Employee ID to edit Department : "))
        print()
        
        if id in db:
            edit_sal = eval(input("Enter the Salary you want to update : "))
            print()
            db[id]['Salary'] = edit_sal
            print(f"You have successfully edit the Department to {edit_sal}",end ='\n\n')
    
    else : 
        print("Please select the appropriate input...", end = '\n\n')
    
        
def delete () :
    length ()
    id = eval(input("Enter the Employee ID : "))
    print()
    
    if id in db:
        del db[id]
        print("You have successfully deleted the Employee Details...")
    else:
        print("Enter Valid ID....")
        
def search () :
    length ()
    
    dep = input("Enter the department you want to search with : ").title()
    
    for i in db.values () :
        if (i['Dept']) == dep :
            print (i['Empid'])
 
    
    
while True :
    
    dashboard ()
    
    ch = int(input("Enter the input you want to : "))
    
    if ch == 1:
        add()
    
    elif ch == 2:
        display()
    
    elif ch == 3:
        edit ()
    
    elif ch == 4:
        delete ()
    
    elif ch == 5:
        search ()
    
    else :
        print("Enter the valid input ....")
        
    choice = input("Do you want to continue (y/n) : ").lower()
    print()
    
    if choice == 'n':
        print("Ok.. Thank you...")
        break   
    