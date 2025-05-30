
year = int(input("Which year you want to check!"))

def is_leap(year):
    if year % 2 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
               return True
            else:
                return False
        else:
           return True
    else:
        return False


def day_in_month(year, month):
   month_days =[31, 28, 31, 30, 31, 30, 31, 31]
   if is_leap and month == 2:
       return 29
   else: 
        return month_days[month - 1]
       
result = is_leap(int(input("Which year you want to check!")))


print(result)