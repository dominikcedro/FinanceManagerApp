# the whole idea is, if you input 2024-01.01 10:10:10 it
# should tell which year is it (leap or not) and provoide you with
# days that february will have
from datetime import datetime
def is_leap_year(date: str):
    date_obj = datetime.strptime(date, '%Y-%m-%d %H:%M:%S')
    if date_obj.year % 4 == 0:
        return True
