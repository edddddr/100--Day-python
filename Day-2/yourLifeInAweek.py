# how many time do you left from your age, If you are leave for 90 years

days = 365 * 90
week = 52 * 90
month = 12 * 90

userage = int(input("What is your current age? "))

userDays = userage * 365
userWeek = userage * 52
userMonth = userage * 12

print(f"You have {days - userDays} days, {week - userWeek} Weeks, and {month - userMonth} months left. Have a nice years 😊")
