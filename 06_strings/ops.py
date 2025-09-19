# String Methods

# simulate gmail user id input formatting 
email = input("Enter Your ID: ")
format_email = email.lower() + "@gmail.com"
print("Original Input: "+email)
print("Formatted Output: "+format_email)

# simulate PAN 

pan = input("Enter Your PAN ID: ")

if pan.isalnum(): 
    format_pan = pan.upper()
    print("User given PAN: "+pan)
    print("Formatted PAN: "+format_pan)
else:
    print("User given PAN is invalid: "+pan)


# redirect call based on isd code 
mobile_num = input("Enter Mobile Number with ISD code: ")
if mobile_num.startswith("+91"):
    print("Calling India")
elif mobile_num.startswith("+1"):
    print("Calling USA")
elif mobile_num.startswith("+86"):
    print("Calling China")
else:
    print("Calling support available only to India, USA & China")

# email synchronization 
source_email = input("Enter Your Email ID: ")
destination_email = input("Enter Your Email ID: ")

if source_email.endswith("@gmail.com") and destination_email.endswith("@gmail.com"):
    print("synchronizing email")
else:
    print("synchronizing failed both providers should of same type")

#gmail removes spaces at the beginnigna nd at the ending of the email provided 

# csv /excel lot of data in rows
# Name, City, Age, Email, Role 
emp_row = "john,Hyd,205,john@gmail.com,Developer"
print("Original Data: "+emp_row)

fields = emp_row.split()
print(fields)

# print emp name and role
print("Name: "+fields[0])
print("Role: "+fields[4])

# 


