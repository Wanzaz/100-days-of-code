import datetime as dt

now = dt.datetime.now()
year = now.year
month = now.month
day_of_week = now.weekday

date_of_birth = dt.datetime(year=2000, month=10, day=10, hour=10)
print(date_of_birth)
