import datetime
import time
from dateutil.relativedelta import relativedelta

print(datetime.datetime.now())

epoch = 1485789600
print(datetime.datetime.fromtimestamp(epoch))
#          year  month day   hour min  s  
bd_tuple = 1975,     2, 23,     4,  0, 1, 0,0,0    
birthday = time.mktime(bd_tuple)
print(birthday)

alter = time.time() - birthday
print(alter / (365.24 * 24 * 3600))

dt_birthday = datetime.date(1975,2,23)
dt_today    = datetime.date.today()

diff = dt_today - dt_birthday

age = (relativedelta(dt_today, dt_birthday))
print(age.years, age.months, age.days)