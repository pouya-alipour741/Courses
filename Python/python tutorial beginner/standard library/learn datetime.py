import datetime
import pytz
# d = datetime.date.today()
# print(d.month)

# tday = datetime.date.today()
# tdelta = datetime.timedelta(days=7)
# print(tday - tdelta)

# bday = datetime.date(2023, 4, 6)
# bd_delta = bday - tday
# print(bd_delta.total_seconds())

# t = datetime.time(9,50,45,9000)
# print(t)

# dt = datetime.datetime(2022,8,25,23,4,59,600)
# dt_delta = datetime.timedelta(hours=2)
# print(dt + dt_delta)

# dt = datetime.datetime(2022,8,25,23,4,59,600,tzinfo=pytz.UTC)
# print(dt)
dt_utcnow = datetime.datetime.now(tz=pytz.UTC)
# print(dt_utcnow)
dt_tehnow = dt_utcnow.astimezone(pytz.timezone('asia/tehran'))
# print(dt_tehnow)

# for tz in pytz.all_timezones:
#     print(tz)

# print(dt_tehnow.strftime('%B %d, %Y')) #datetime to string
# dt_tehnow_str = 'September 01, 2022'
# print(datetime.datetime.strptime(dt_tehnow_str,'%B %d, %Y')) #string to datetime
print(dt_tehnow)

print(dt_tehnow.strftime('%b %d, %y - %A - %I:%M:%S %p - %Z'))
dt_tehnowstr = 'Sep 03, 22 - Saturday - 12:36:56 PM'
print(datetime.datetime.strptime(dt_tehnowstr, '%b %d, %y - %A - %I:%M:%S %p'))

