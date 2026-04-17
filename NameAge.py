import datetime

user_name = input('What is your name?')
user_age = int(input('How old are you?'))


today = datetime.date.today()
year = today.year
year_born = (year - user_age)

print()
print("Hello", user_name.strip() + "! You were born in", str(year_born) + ".")