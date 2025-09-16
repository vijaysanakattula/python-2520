# Simulate OTP/PIN/PASSWORD Verification System

# actual_otp = 8901
# module random
import random
actual_otp = random.randint(1000,9999)
print(actual_otp)

attempts = 3 

while attempts:
    user_otp = int(input("Enter OTP: "))
    if len(str(user_otp)) !=4:
        print("OTP must be 4 Digits only")
    if user_otp == actual_otp:
        print("Correct OTP - Transaction Success")
        break
    attempts = attempts - 1 

else:
    print("maximum attempts reached, try after 24 hours")
