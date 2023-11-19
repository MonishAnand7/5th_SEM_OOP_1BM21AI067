import re

def IsValidEmail(email):
    pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'

    if re.match(pattern, email):
        return True
    else:
        return False

user_email = input("Enter an email address: ")
result = IsValidEmail(user_email)

if result:
    print(f"{user_email} is a valid email address.")
else:
    print(f"{user_email} is not a valid email address.")
