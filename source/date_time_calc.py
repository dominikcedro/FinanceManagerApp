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

def days_in_month(int_month:int,is_leap=bool):

    dict_month = {1:31, 2:28, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}
    if is_leap:
        dict_month[2] = 29
    return dict_month[int_month]