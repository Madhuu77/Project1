import random
def Generate_OTP():
    otp=""
    for i in range(6):
        otp+=str(random.randint(0,9))
    return otp
print("Your OTP is:",Generate_OTP())