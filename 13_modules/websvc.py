# Working with some API -> Fullstack 
import requests
service_url = "https://www.python.org/"

response = requests.get(service_url)
print(response.status_code)

service_url = "https://www.python.org/vijay"

response_code = requests.get(service_url)
print(response_code.status_code)