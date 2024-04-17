from datetime import datetime


def string_to_date(date_string):
    return datetime.strptime(date_string, "%Y.%m.%d").date()


def prepare_user_list(user_data):
    dict_user = []
    for key in user_data:
        dict_user.append(
            {
                "name": key["name"],
                "birthday": string_to_date(key["birthday"]),
            }
        )
    return dict_user


users = [
    {"name": "Bill Gates", "birthday": "1955.3.25"},
    {"name": "Steve Jobs", "birthday": "1955.3.21"},
    {"name": "Jinny Lee", "birthday": "1956.3.22"},
    {"name": "John Doe", "birthday": "1985.01.23"},
    {"name": "Jane Smith", "birthday": "1990.01.27"},
]

prepared_users = prepare_user_list(users)
print(prepared_users)
