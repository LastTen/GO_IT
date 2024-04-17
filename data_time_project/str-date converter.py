from datetime import datetime


def string_to_date(date_string):
    date_obj = datetime.strptime(date_string, "%Y.%m.%d").date()
    return date_obj


def date_to_string(date):
    str_date = datetime.strftime(date, "%Y.%m.%d")
    return str_date


date_string = "2024.01.01"

print((string_to_date(date_string)))

print((date_to_string(string_to_date(date_string))))
