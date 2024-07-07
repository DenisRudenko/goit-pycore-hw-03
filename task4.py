import datetime


def get_upcoming_birthdays(users: list):
    celebrators = []
    for user in users:
        parsed_birthday = datetime.datetime.strptime(user['birthday'], '%Y.%m.%d').date()
        today = datetime.date.today()

        # Add a day or two for congratulation date if birthday is on a weekend:
        def calculate_congrats_day(date: datetime.date):
            if date.weekday() == 5:
                return date + datetime.timedelta(days=2)
            elif date.weekday() == 6:
                return date + datetime.timedelta(days=1)
            return date

        # Check b-day this year:
        this_year_birthday = parsed_birthday.replace(year=today.year)
        if this_year_birthday >= today:
            if 0 <= (this_year_birthday - today).days <= 7:
                this_year_birthday = calculate_congrats_day(this_year_birthday)
                celebrators.append({'name': user['name'], 'congratulation_date': this_year_birthday})
            continue

        # Check if less than 7 days left to the new year:
        if today.month == 12 and today.day > 25:
            # Check b-day next year:
            next_year_birthday = parsed_birthday.replace(year=today.year + 1)
            if (next_year_birthday - today).days <= 7:
                next_year_birthday = calculate_congrats_day(next_year_birthday)
                celebrators.append({'name': user['name'], 'congratulation_date': next_year_birthday})

    return celebrators


users = [
    {"name": "John Doe", "birthday": "1985.01.04"},
    {"name": "Jane Smith", "birthday": "1990.07.06"}
]

upcoming_birthdays = get_upcoming_birthdays(users)
print("Список привітань на цьому тижні:", upcoming_birthdays)
