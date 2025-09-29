# Arbitrary Positional Arguements(*args)
def add_all(*numbers): 
    total = 0 
    for num in numbers: 
        total = total + num 
    print (f"The Total Sum is {total}")

add_all(10)
add_all(10,20)
add_all(10,20,30,40,50)


# Arbitrary Keywords Arguements (**kwargs)
def profile(**info):
    print(info)

profile(name="Vijay")
profile(name="Vijay",location="hyd",age=30)

def cred_trans(**trans):
    print(trans)
    total = 0 
    for tran in trans:
        print(tran)
cred_trans(jan=1000,feb=2000,mar=3000)

# NOTE : just like dict it's considering only keys 

# To get value => we need key 
def cred_trans(**trans):
    print(trans)
    total = 0 
    for tran in trans:
        print(trans[tran])
cred_trans(jan=1000,feb=2000,mar=3000)

# using both to do some calculation 
def cred_trans(**trans):
    print(trans)
    total = 0 
    for tran in trans:
        total = total + trans[tran]
        # print(trans[tran])
    print(f"You have done {len(trans)} which amounts to total of {total}")
cred_trans(jan=1000,feb=2000,mar=3000)

# without return keyword 
def add(a,b):
    a+b

add(10,20)
print(add(10,20))

# with return keyword 
def add(a,b):
    return a+b

add(10,20)
print(add(10,20))

# 
def add(a,b):
    return a+b
    print("See if this will be printed")

print(add(10,20))

def math_ops(a,b):
    return a+b
    return a*b
    return a/b

print(math_ops(100,200))

def math_ops(a,b,opr):
    if opr == "+":
        return a+b
    elif opr =="*":
        return a*b
    elif opr =="/":
        return a/b
    else:
        return "Invalid Operator Selected"
    
print(math_ops(100,200,"+"))
print(math_ops(100,200,"*"))
print(math_ops(100,200,"-"))

# Function Composition
def add(a,b):
    return a+b

def sub(c,d,e):
    return add(c,d) - e

print(sub(3,4,5)) # add c & d from that minus - e # 2 

# local scope 
def add(): 
    # local variables 
    la = 10 
    lb = 5
    print(la) # access local variable within function 
    print(lb) # access local variable within function 

add()

# trying to access local variable outsie the function 
# print(la)

# local scope 
def add(la,lb):
     print(la) # access local variable within function 
     print(lb) # access local variable within function

add(30,20)

# tring to access local variable outsie the function
# print(la)
