# Q. Find factorial?

def fact (num):
    if num == 0:
        return 1
    else :
        return num * fact(num-1)

num = eval(input("Enter the number : "))
factorial = fact(num)
print(factorial)