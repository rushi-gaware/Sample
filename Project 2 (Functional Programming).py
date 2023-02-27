db = {1 : {'Name' : 'Rushi' , 'Subject':'Science' , 'Std' : 10 ,'Age' : 15 ,'Mobile' : 8657730558 , 'RollNo' : 1 },
      2 : {'Name' : 'Shreya' , 'Subject' : 'Drawing' , 'Std' : 9 , 'Age' : 16 , 'Mobile' : 8017993204 ,  'RollNo' : 2},
      3 : {'Name' : 'Mimi' , 'Subject' : 'Sleeping' , 'Std' : 1 , 'Age' : 2 , 'Mobile' : 8888888888 , 'RollNo' : 3}
      }

def dashboard () :

    print ('*' * 30, "Welcome to Student Management System", '*' * 30)
    
    print('''
          
                                 1. Add New Student Details
                                 2. Display All Student Details
                                 3. Edit Student Details
                                 4. Delete Student Details          
          
          ''')

    print('*' * 100)
    
    
def len () :
    if db.keys() == 0:
        print("Your Datanase is Empty......")
        

def add () :
    len ()
    
    u_name = input("Enter Student's Name : ").title()
    u_subject = input("Enter Student's Subject : ").title()
    u_std = eval(input("Enter Student's Std : "))
    u_age = eval(input("Enter Student's Age : "))
    u_mobile = eval(input("Enter Student's Mobile Number : "))
    u_roll = eval(input("Enter Student's Roll Number : "))
    
    dict = {}
    
    dict['Name'] = u_name
    dict['Subject'] = u_subject
    dict['Std'] = u_std
    dict['Age'] = u_age
    dict['Mobile'] = u_mobile
    dict['RollNO'] = u_roll
    
    db[u_roll] = dict
    
    print("You have successfully added {u} in the Database".format (u = u_name))


def display () :
    len ()
    
    print('-' * 120,end = '\n')
    print(" {n:^20} | {s:^20} | {st:^20} | {a:^20} | {m:^20} | {r:^20} | ".format (n = 'Name' , s = 'Subject' , st = 'STD' , a = 'Age', m = 'Mobile' , r = 'Roll No'),end = '\n')
    
    for i in db.values() :
        print('-' * 120,end = '\n')
        print(" {name:^20} | {sub:^20} | {std:^20} | {age:^20} | {mobile:^20} | {rollno:^20} | ".format (name = i['Name'] , sub = i['Subject'] , std = i['Std' ] ,  age = i['Age'] , mobile = i['Mobile'] , rollno = i['RollNo']))
        
def edit ():
    len()
    rollno = eval(input("Enter the Roll Number you want to do the Updation with : "))
    
    if rollno not in db :
        print("Can't Find in the database... Enter Valid input....")
        print()
        
    else : 
        print('''
            
                       1.Edit name
                       2.Edit Subject
                       3.Edit STD
                       4.Edit Age
                       5.Edit Mobile number
                       
       ''' )
        
        choice = eval(input("Select the input from above options : "))
        print()
        
        if choice == 1 :
            edit_name = input("Enter the Edited name : ")
            
            db[rollno]['Name'] = edit_name 
        
        if choice == 2 :
            edit_sub = input("Enter the Edited Subject Name : ")
            
            db[rollno]['Subject'] = edit_sub
            
        if choice == 3 :
            edit_std = eval(input("ENter the Edited Standard : "))
            
            db[rollno]['Std'] = edit_std
            
        if choice == 4 :
            edit_age = eval(input("Enter the Updated Age : "))
            
            db[rollno]['Age'] = edit_age
    
        if choice == 5 :
            edit_roll = eval(input("Enter the edited Mobile Number : "))
            
            db[rollno]['RollNo'] = edit_roll
            
        elif choice > 5 :
            print("Please Select Valid input......")
            
def delete () :
    len()
    
    rollno = eval(input("Enter the Roll Number you want to Remove : "))
    
    if rollno not in db :
        print("Can't Find in the database... Enter Valid input....")
        print()
    else :
        del db[rollno]
        
        print("You have successfully deleted from the database...")

while True :

    dashboard ()
    
    ch = eval(input("What would you like to do : "))
    print()
    
    
    if ch == 1 :
        add ()
    
    if ch == 2:
        display ()
    
    if ch == 3:
        edit ()
    
    if ch == 4:
        delete ()
    
    elif ch > 4 :
        print("Please select the Valid Input.........")
    
    choice = input ("Would you like to continue (y/n) : ").lower()
    
    if choice != 'y':
        print('\n\n' "Okay, Thank You.......")
        break 