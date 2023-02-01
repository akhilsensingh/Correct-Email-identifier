import re #regex importing Regular Expresssion
condition = "^[a-z]+[\._]?[a-z 0-9]+[@]\w+[.]\w{2,3}$"  
                         #All condition is define in on variable
                         #^ this is use to make conditon read from start like 1 to 10.
                         # + this symbol concatinate the all condition.\ is use to search any character in regix.
                         # ? this works on 0 or 1 like true or false, mention outside the conditional brackets.
                         # \w searh the string +{}we mention condition in these bracses
                         #$ this is use to search from backside.
email = input("Enter your email :: ")
                         #taken user input
if re.search(condition,email):
    print("Right email")
else:
    print("Wrong email")