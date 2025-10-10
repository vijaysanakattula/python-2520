# Working with JSON Data

import json

student = {
    "id": 101,
    "name": "Vijay",
    "course": "Python Full Stack",
    "skills": ["Python", "Git", "AWS"],
    "score": 60
}

print(type(student))

# Writing to JSON file without Indentation 
with open("14_file_operations/student.json","w") as file_data:
    json.dump(student,file_data)


# Writing to JSON file with Indentation 
with open("14_file_operations/student.json","w") as file_data:
    json.dump(student,file_data,indent=1)


# Writing to JSON file with recommended Indentation is 4
with open("14_file_operations/student.json","w") as file_data:
    json.dump(student,file_data,indent=4)

# Reading JSON File 
with open("14_file_operations/student.json","r") as file_data:
    json_reader = json.load(file_data)
print(json_reader)
print(type(json_reader))

# Get the student name
with open("14_file_operations/student.json","r") as file_data:
    json_reader = json.load(file_data)
print(json_reader["name"])

# Check student passed if score above 75 
if json_reader["score"] > 75:
    print(f"{json_reader["name"]} not passed")


student = {
    "id": 101,
    "name": "Vijay",
    "course": "Python Full Stack",
    "skills": ["Python", "Git", "AWS"],
    "score": 60
}

print(type(student))

python_object = json.dumps(student)
print(python_object)
print(type(python_object))

json_string = '{"id": 101, "name": "Vijay", "course": "Python Full Stack", "skills": ["Python", "Git", "AWS"], "score": 60}'
print(type(json_string))
python_object = json.loads(json_string)
print(python_object)
print(type(python_object))

# working with users API 
with open("14_file_operations/users.json","r") as file_data:
    data = json.load(file_data)
print(data)
print(type(data))

# Req : get me number of users in our system 
total_users = len(data['users'])
print("total Users In System: ",total_users)

# Req : get me all users data whose age is below 30 
with open("14_file_operations/users.json","r") as file_data:
    data = json.load(file_data)
    for user in data['users']:
        # print(user)
        if user['age'] < 30:
            # print(user)
            print(user['username'], user['age'])
