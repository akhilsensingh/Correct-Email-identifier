import re
condition = "^[a-z]+[\._]?[a-z 0-9]+[@]\w+[.]\w{2,3}$"  

email = input("Enter your email :: ")

if re.search(condition,email):
    print("Right email")
else:
    print("Wrong email")
