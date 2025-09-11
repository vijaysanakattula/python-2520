# Working with Variables

# Assigning Data
student_name = "vijay"
student_age = 20
student_gpa = 9.5
student_passed = True

# Retreive Data
print(student_name)
print(student_age)
print(student_gpa)
print(student_passed)


# Data
print(id(student_name))
print(id(student_age))
print(id(student_gpa))
print(id(student_passed))

list_nums_a = [10,20,30,40,50]
print(type(list_nums_a))
print(id(list_nums_a))

list_nums_b = [10,20,30,40,50]
print(type(list_nums_b))
print(id(list_nums_b))

# To access data inside list we use index -> index starts from 0 1 2 ...
# 0. 1. 2. 3. 4.
# [10,20,30,40,50]
print(list_nums_a) # print entire list
print(list_nums_b) # print entire list


print(type(student_name))
print(type(student_age))
print(type(student_gpa))
print(type(student_passed))


name = "Vijay"
age = 20


# old style of python
print("my name is ", name + " and my age is ", age)

print("My name is {name} and my age is {age} after 5 years my age is {age+5}") # no f string
print(f"My name is {name} and my age is {age} after 5 years my age is {age+5}") # f string



x,y,z = 10,20,30
print(x)
print(y)
print(z)

a = 10
b = 20
c = 10
d = 10 

a = c = d = 10
print(a)
print(c)
print(d)