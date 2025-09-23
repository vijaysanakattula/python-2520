# Dictionary 

# empty dict 
empty_dict = {}
print(type(empty_dict))
print(empty_dict)

# empty dict using class
empty_dict = dict()
print(type(empty_dict))
print(empty_dict)

# store data 
dict_nums = {1:10,2:20,3:30}
print(type(dict_nums))
print(dict_nums)

dict_text = {"one:ten","two:twenty","three:thirty"}
print(dict_text)

mixed_data = {1:10,"two":"twenty","three":3}
print(mixed_data)

# duplicate with keys
dict_nums = {1:10,2:20,3:30,2:200}
print(dict_nums)

# duplicate with values
dict_nums = {1:10,2:20,3:30,4:20}
print(dict_nums)

# keys cannot be mutable (lists are mutable)
# dict_data = {[10]:100} # TypeError: unhashable type: 'list'
dict_data = {"data":[10,20,30]}
print(dict_data)
dict_data = {(10):100}
print(dict_data)

# loop the data 
dict_nums = {1:10,2:20,3:30}
print(dict_nums)
print(dict_nums[2])

# only we get keys 
for data in dict_nums:
    print(data)

print(dir(dict_nums))


