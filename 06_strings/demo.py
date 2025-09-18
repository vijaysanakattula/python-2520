# string concatenation
s = "good"
m = " morning"
print(s+m)

a = 10
b = 20
print(a+b)

# string formatting
age = 30
# print("My age is: "+age) # TypeError: can only concatenate str (not "int") to str

# interpolation - {}
print(f"My age is: {age}")
print(f"My age is: ",age)
print(f"My age is: ", +age)
print(f"My age is: "+str(age))

# print("My age after 5 years would be: ", +age+5")

greet = "hello"
print(greet)
greet = "Hello"
print(greet)

# String Immutability
# Immutable : cannot be changed 
greet = "hello"
print(greet)
#greet[0] = "H" # TypeError: 'str' object does not support item assignment
print(greet)



