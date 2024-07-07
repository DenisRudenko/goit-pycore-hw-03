import datetime


def get_days_from_today(date):
    try:
        parsed_input_date = datetime.datetime.strptime(date, '%Y-%m-%d').date()
        # today = datetime.date.today()
        today = datetime.datetime.strptime('2021-05-05', '%Y-%m-%d').date()
        delta = (today - parsed_input_date).days

        return print(f"Difference in days between {today.strftime('%Y-%m-%d')} and inputted date:{parsed_input_date} is: {delta}")
    except ValueError:
        print(f"Inputted date:'{date}' has invalid date format.")
        # Retry block:
        try_again = input("Do you want to try again? (Y/N): ")
        if try_again.lower() == 'y':
            new_date = input("Enter a date in the format YYYY-MM-DD: ")
            return get_days_from_today(new_date)
        else:
            return "Goodbye!"


test_time = input("Enter a date in the format YYYY-MM-DD: ")
print(get_days_from_today(test_time))
