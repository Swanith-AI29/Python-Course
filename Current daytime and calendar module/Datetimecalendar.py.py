from datetime import date,time,datetime
import calendar
today=date.today()
print(today)
now=datetime.now()
print(now)
print(today.year,today.month,today.day)
year=2025
month=11
print(calendar.month(year,month))
