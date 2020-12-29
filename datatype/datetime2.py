"""
calculate date by day interval
"""
import datetime

begin2000 = datetime.date(2000, 1, 1)
# what is the date after 100 days?
delta = datetime.timedelta(days=100) # default is days
after100 = begin2000 + delta
print(after100)

today = datetime.datetime.today()
# what is the time after 100 hours? (plan to do something in 100 hours, figure out exactly date and time)
delta = datetime.timedelta(hours=100)
after100hours = today + delta
print(after100hours)