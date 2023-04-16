"""
Other than Python language intrinsic data type,
python also built in a lot of other data type, such as datetime

https://docs.python.org/3/library/datetime.html
"""
import datetime
"""
>>> import datetime
>>> dir(datetime)
['MAXYEAR', 'MINYEAR', '__all__', '__builtins__', '__cached__', '__doc__', 
'__file__', '__loader__', '__name__', '__package__', '__spec__', 'date', 
'datetime', 'datetime_CAPI', 'sys', 'time', 'timedelta', 'timezone', 'tzinfo']
"""

birthday = datetime.date(1958,7,8) # Python creator Guido Van Rossum
print(birthday)
print(type(birthday))

a = 5
print(type(a)) # both datetime.date and int are Python class, there is no difference between

print(birthday.day)
print(birthday.month)
print(birthday.year)

today = datetime.date.today()
print(today)

# math
age = today.year - birthday.year
print(age)

diff = today-birthday
print(diff.days/365)