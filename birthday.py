import datetime


def get_birthdays_per_week(users):
    birthday_this_week = {}
    datetime_now = datetime.datetime.now().date()
    end_data = datetime_now + datetime.timedelta(
        days=7)

    for i in users:
        date_user = datetime.datetime.strptime(i.get('birthday'),
                                               '%Y-%m-%d').date()
        if datetime.timedelta(days=0) <= end_data - date_user \
                <= datetime.timedelta(days=7):
            if date_user.weekday() == 5 or date_user.weekday() == 6:
                birthday_this_week.setdefault('Monday',
                                              []).append(i.get('name'))
            else:
                birthday_this_week.setdefault(date_user.strftime('%A'),
                                              []).append(i.get('name'))

    return birthday_this_week


def normalize_birthdays(users):
    normalize_birthdays = []
    data_now = datetime.datetime.now()
    for i in users:
        data_user = datetime.datetime.strptime(i.get('birthday'), '%Y-%m-%d')
        if data_user.year != data_now.year:
            date_user_norm = datetime.datetime(data_now.year, data_user.month,
                                          data_user.day).date()
            i['birthday'] = str(date_user_norm)
            normalize_birthdays.append(i)
        else:
            normalize_birthdays.append(i)
    return normalize_birthdays


def print_birthdays(users):
    for i in users:
        print(i + ':', ', '.join(users[i]))


users = [
    {'name': 'Bill', 'birthday': '2023-02-12'},
    {'name': 'Jill', 'birthday': '2021-02-13'},
    {'name': 'Lil', 'birthday': '2022-02-14'},
    {'name': 'Smit', 'birthday': '2022-02-5'}
]

print_birthdays(get_birthdays_per_week(normalize_birthdays(users)))
