import datetime
def sun(year):
    date=datetime.date(year,1,1)
    date+=datetime.timedelta(days=(6-date.weekday()))
    while date.year==year:
        yield date
        date+=datetime.timedelta(days=7)
def print_sunday(year):                    
    for sunday in sun(year):
       print(sunday) 
year=2023
print("all sundays in",year)
print_sunday(year)      



