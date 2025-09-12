#int type
data = 10
print(type(data))

#float type
data = 10.5
print(type(data))

#complex type
data = 3 + 5j
print(type(data))

#string type
data = "python"
print(type(data))

#boolean type
data = False
print(type(data))

# List (homogenous data)
data = [10,20,30,40,50]
print(type(data))

# Tuple (heterogenous data)
data = (101,"Vijay",True)
print(type(data))

# Set
data = {10,20,30,40,50}
print(type(data))

# Dictionary
data = {"name":"Vijay", "id":101, "location":"hyd"}
print(type(data))

# None Type
x = None
print(type(x))

# User defined datatype
class Student: 
    #logics
    pass # syntax
student_john = Student()
print(type(student_john)) # <class '__main__.Student'> --> '__main__.Student' indicate user defined datatype


# Type Conversion
a = 10 # int
print(type(a))
b = 3.5 # float
print(type(b))
c = a + b # dynamic
print(c)
print(type(c))

# Type Casting 
pi = 3.14 # float
print(type(pi))
print(pi)

# requirement round of pi and give whole number 
pi_round_int = int(pi)
print(type(pi_round_int))
print(pi_round_int)

rating = "4"
# increment_rating = rating + 1 #TypeError: can only concatenate str (not "int") to str
increment_rating = int(rating) + 1
print(increment_rating)
print(type(increment_rating))


