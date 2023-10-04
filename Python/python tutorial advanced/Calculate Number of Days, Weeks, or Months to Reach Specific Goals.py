import datetime
import calendar
import math

#1 calculatedelete remaining debt
# credit_balance = 10000
# interest_rate = 13 * 0.01
# payment = 1000
#
# my_date = datetime.datetime.today()
# month_range = calendar.monthrange(my_date.year,my_date.month)[1]   #returns a tuple of day of the week that the first day of month falls on and total number of days in that month
#
# days_until_month_end = month_range - my_date.day
# start_date = my_date + datetime.timedelta(days=days_until_month_end+1)
#
# end_date = start_date
# while credit_balance > 0:
#     interest_charge = (interest_rate/12) * credit_balance
#     credit_balance += interest_charge
#     credit_balance -= payment
#
#     credit_balance = round(credit_balance,2)  #can use None instead of 2
#     if credit_balance < 0:
#         credit_balance = 0
#     print(end_date,f'{(end_date - my_date).days} days',credit_balance,sep='--')
#     month_range = calendar.monthrange(end_date.year, end_date.month)[1]
#     end_date += datetime.timedelta(days=month_range)

#2 calculatedelete target weight
# weight = 80
# target_weight = 90
# weekly_gain = 0.3
#
# start_date = datetime.date.today()
#
# end_date = start_date
# while weight < target_weight:
#     weight += weekly_gain
#     end_date += datetime.timedelta(days=7)
#     print(f'reached goal in {(end_date - start_date).days//7} weeks',weight)
# print(end_date)

#3 method 1 hit target subscribers
current_subs = 8700
target_subs = 10000
avg_daily_sub = 11

start_date = datetime.date.today()

end_date = start_date
while current_subs < target_subs:
    end_date += datetime.timedelta(days=1)
    current_subs += avg_daily_sub
    print((end_date-start_date).days,current_subs)

# #method 2
# current_subs = 8700
# target_subs = 10000
# avg_daily_sub = 11
# sub_to_go = target_subs - current_subs
# days_to_go = math.ceil(sub_to_go / avg_daily_sub)
# start_date = datetime.date.today()
# print(start_date + datetime.timedelta(days=days_to_go))

