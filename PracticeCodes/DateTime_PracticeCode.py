import datetime

# print(datetime.datetime.now().time().hour)

date = datetime.datetime.now().date().strftime("%A, %d %B %Y")
print(f"\nBoss the date is: {date}")