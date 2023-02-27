### 2. Iteration Statemnt

# A. For Loop

# B. While Loop - We sue when we don't know the number of iteration
# i). Using ICU Method (Initialisation - Condition - Update)

i = 78   # Initialization

while i <= 780:   # Condition
    print(i)
    i += 78         # Update (Increment or decrement)
    

# ii). Direct mehtod

while True:
    print("Rushi")
    ch = input("Do you want to print again (Y/N) :").lower()
    if ch != 'y':
        print("OK.........")
        break
    
############ Transfer control statement
#1. break
#2. continue
#3. pass

l = [234,45,564,35,-35,-34,0,-23,245,8675]

for i in l:
    if -21 > i >-24 :
        if i%2 == 1:
            print("This is negative number", i)
    else:
        pass
    
    
li = [10,-20,33,-455,30]
l = len(li)
ra = range(l)

for i in ra:
    if  li[i] >= 1:
        print(li[i],"is positive and is at index : ",i)
    else:
        pass
    
