from datetime import datetime, timedelta


def string_to_date(date_string):
    return datetime.strptime(date_string, "%Y-%m-%d").date()


def find_next_weekday(start_date, weekday):
    days_ahead = weekday - start_date.weekday()
    if days_ahead <= 0:
        days_ahead += 7
    return start_date + timedelta(days=days_ahead)


def adjust_for_weekend(birthday):
    if birthday.weekday() >= 5:  # Якщо день народження підпадає на вихідний (сб або нд)
        next_monday = find_next_weekday(birthday, 0)  # Знаходимо наступний понеділок
        return next_monday
    else:
        return birthday
