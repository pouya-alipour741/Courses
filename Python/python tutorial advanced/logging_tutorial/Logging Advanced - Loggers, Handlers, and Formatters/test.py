import datetime
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.WARNING)

formatter = logging.Formatter('%(asctime)s:%(name)s:%(message)s')

filehandler = logging.FileHandler('calc.log')
filehandler.setFormatter(formatter)

streamhandler = logging.StreamHandler()
streamhandler.setFormatter(formatter)
# streamhandler.setLevel(logging.ERROR)

logger.addHandler(filehandler)
logger.addHandler(streamhandler)

current_subs = 8700
target_subs = 10000
avg_daily_sub = 11

logger.error(current_subs)

start_date = datetime.date.today()

end_date = start_date
while current_subs < target_subs:
    end_date += datetime.timedelta(days=1)
    current_subs += avg_daily_sub
    # print((end_date-start_date).days,current_subs)



