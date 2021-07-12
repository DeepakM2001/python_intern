import datetime

def convert(date_time):
    format = '%b %d %Y %I:%M%p' # The format
    datetime_str = datetime.datetime.strptime(date_time, format)
    return datetime_str

date_time = 'Mar 24 2021 07:54PM'
print(convert(date_time))
