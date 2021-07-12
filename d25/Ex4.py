import datetime
base = datetime.datetime.today()
for x in range(0, 7):
    print(base + datetime.timedelta(days=x))
