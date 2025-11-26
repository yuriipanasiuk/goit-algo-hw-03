from datetime import datetime, timedelta


def get_upcoming_birthdays(users):
    today = datetime.today().date()
    date_format = "%Y.%m.%d"
    user_birthdays = []

    for user in users:
        user_birthday = datetime.strptime(user["birthday"], date_format).date()
        birthday_this_year = user_birthday.replace(year=today.year)

        if birthday_this_year < today:
            birthday_this_year = user_birthday.replace(year=today.year + 1)

        days_to_birthday = (birthday_this_year - today).days
        if 0 <= days_to_birthday <= 7:
            if birthday_this_year.weekday() == 5:
                congratulation_date = birthday_this_year + timedelta(days=2)

            elif birthday_this_year.weekday() == 6:
                congratulation_date = birthday_this_year + timedelta(days=1)

            else:
                congratulation_date = birthday_this_year

            user_birthdays.append(
                {
                    "name": user["name"],
                    "congratulation_date": congratulation_date.strftime(date_format),
                }
            )

    return user_birthdays


users = [
    {"name": "John Doe", "birthday": "1985.11.10"},
    {"name": "Jane Smith", "birthday": "1990.11.09"},
]


upcoming_birthdays = get_upcoming_birthdays(users)
print("Список привітань на цьому тижні:", upcoming_birthdays)
