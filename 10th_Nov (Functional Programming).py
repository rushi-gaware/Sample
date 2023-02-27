

a = 10                        # Global Scope
def math ():
    b = 20                    # Local Scope
    c = 30
    sum = (a+b+c)
    sub = (a-b-c)
    mul = (a*b*c)
    print(sum,sub)
    return mul                # LocL scope value is returned to global scope

res = math()                  # Global Scope # Function is called
print(res)