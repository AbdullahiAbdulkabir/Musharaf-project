
from datetime import date
import datetime, calendar

year = int(input("Please input the next year or current year for birthday "))
month = int(input("Input the month in the range of 1 to 12 i.e 3(april) "))
day = int(input("input the day "))

my_date = datetime.datetime(year, month, day)
day_in_week = calendar.day_name[my_date.weekday()]
print(day_in_week)
