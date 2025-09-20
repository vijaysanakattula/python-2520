# Lists 

# emplty lust 
empty_list = []
print(type(empty_list))
print(empty_list)

# empty list using class
empty_list = list()
print(type(empty_list))
print(empty_list)

# list data 
num_list = [10,20,30,40,50] #homogenous
print(num_list)

num_list = list([10,20,30,40,50])
print(num_list)

text_list = ["python","cloud","django","ai"]
print(text_list)

mixed_list = [10,20,30,"python","cloud",5.5,True] #heterogenous
print(mixed_list)

single_element = [10]
print(single_element)

single_element = list([10])
print(single_element)

# Access data
num_list = [10,20,30,40,50] # Homogenous
print(num_list)

# access individual element
print(num_list[0])
print(num_list[3])
print(num_list[-1])
print(num_list[-1]) # out of range 

# access range of elements use slicing 
print(num_list[::])
print(num_list[1:3:])
print(num_list[0:5:2])

# List looping
num_list = [10,20,30,40,50] # Homogenous
print(num_list)
# print(dir[num_list])
for num in num_list:
    print(num)
print("--------")

# Use operators 
for num in num_list:
    print(num * 5)
print("--------")

# use conditionals 
num_list = [10,20,30,43,77,40,50] # Homogenous
for num in num_list:
    if num % 2 ==0:
        print("even",num)

# Duplicates are allowed 
num_list = [10,20,30,43,77,40,50] # Homogenous
print(num_list)
print(dir(num_list))
