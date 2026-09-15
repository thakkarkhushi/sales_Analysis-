def calculate_days_in_month(month, year):
    days_in_month = {
        "january": 31,
        "february": 28,
        "march": 31,
        "april": 30,
        "may": 31,
        "june": 30,
        "july": 31,
        "august": 31,
        "september": 30,
        "october": 31,
        "november": 30,
        "december": 31
    }
    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        days_in_month["february"] = 29
    return days_in_month[month]
month = input("Enter the month: ")
year = int(input("Enter the year: "))
days=calculate_days_in_month(month, year)
print("The number of days in month is",days)