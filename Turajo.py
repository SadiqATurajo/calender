import datetime

name = input("Enter Your Name: ")
year = int(input("Enter Your Year Of Birth: "))
month = int(input("Enter Your Month of Birth: "))
day = int(input("Enter Yor Day Of Birth: "))

years = datetime.datetime(year, month, day)

birth_date = datetime.datetime(year, month, day).date()
birth_day_name = birth_date.strftime("%A")

current_date = datetime.date.today()
age = (current_date.year) - (birth_date.year)

next_birthday = datetime.date(current_date.year, birth_date.month, birth_date.day)
next_birth = (next_birthday - current_date).days

print("Hi!, ", name)
print("Your Are ", age, "Years Old ")
print("You were born on ", birth_day_name)
print("Your Next Birthday is on ",next_birthday)
print("There Are ", next_birth, "Days Left Until Your Next Birthday")