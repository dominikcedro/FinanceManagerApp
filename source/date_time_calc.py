# the whole idea is, if you input 2024-01.01 10:10:10 it
# should tell which year is it (leap or not) and provoide you with
# days that february will have
from datetime import datetime
def is_leap_year(date: str):
    year = datetime.strptime(date, '%Y-%m-%d %H:%M:%S').year
    if year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    elif year % 4 == 0:
        return True
    else:
        return False

def days_in_month(date: str):
    pass
