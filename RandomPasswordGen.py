import random
import string
password_len=12
password=""
val= string.ascii_letters+string.ascii_lowercase+string.ascii_uppercase+string.digits+string.punctuation
for i in range(password_len):
    password+=(random.choice(val))

print("Your random generated password is : ",password)