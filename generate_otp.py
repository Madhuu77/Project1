import random
def Generate_otp(l):
    #code to generate numeric otp
    otp=''.join(random.choices('0123456789',k=l))
   #code to generate alphanumeric otp
   #otp=''.join(random.choices('0123456789AaBaCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz',k=l))
    return otp
otp=Generate_otp(4)
print(otp)
