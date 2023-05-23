import re
name = input("Enter Your Full Name: ")
user_name = input("Enter Your User_Name: ")
password = input("Enter Your Password: ")

valid = True
if not re.search(r'[A-Z]',password):
    print("Password Must Contain Atleast One Uppercase Letter")
valid = False

if not re.search(r'[a-z]',password):
    print("Password Must Contain Lowercase Letter")
valid = False

if not re.search(r'[1-9]',password):
    print("Password Must Contain Atleast One Number Letter")
valid = False

if not re.search(r'\d',password):
    print("Password Must Contain Atleast One Symbol Letter")
valid = False

upper_name = name.upper()
hide_password = 'x' * len(password)
lenght = len(password)

print("Your Full Name Is: ", upper_name)
print("Your User_Name Is: ", user_name)
print("Hidden Password:", hide_password)
print("Password Length:", lenght)