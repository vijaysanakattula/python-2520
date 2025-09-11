num1 = 3
num2 = 2
print(f"Sum of {num1} and {num2} is {num1+num2}")
print(f"modulus of {num1} and {num2} is {num1%num2}")
print(f"Division of {num1} and {num2} is {num1/num2}")
print(f"product of {num1} and {num2} is {num1*num2}")
print(f"Difference of {num1} and {num2} is {num1-num2}")

# Compounr Assigment Operators 
num = 10
num = num + 5
print(num)

# Comparison Operators 
a = 10
b = 5
c = 3
d = 2

print(a == b)
print(a > b)
print(a < b)

# Logical Operators - and, or, not 
res_and = a > b and c < d # T and F -> F
print(res_and)
res_and = a > b and c > d # T and T -> T
print(res_and)

# Membership Operators 
# String is a sequence data type 
data = "python"
is_z_present = "z" in data
print(is_z_present)
is_p_present = "p" in data
print(is_p_present)

# employees 
id = 105
emp_ids = [101,102,103,104,106,107,108,109,110]
is_id_present = 105 in emp_ids
print(is_id_present)

is_id_not_present = id not in emp_ids
print(is_id_not_present)

# Identity Operators - Used to compare 
a = 10
b = 10
print(a == b) # Comparison of values 
print(a is b) # Comparison of memory

