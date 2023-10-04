import datetime
date = datetime.datetime(2022,11,7,12)
print(date)
sentence = f"on {date:%A} of this {date:%B} it will be {date.strftime('%j')} day of year"
print(sentence)
