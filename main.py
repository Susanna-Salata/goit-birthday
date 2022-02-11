from datetime import datetime
import datetime as dt

WEEKDAYS = {0:"Monday", 1:"Tuesday", 2:"Wednesday", 3:"Thursday", 4:"Friday", 5:"Saturday", 6:"Sunday"}


def helper(date_val):
    return dt.date(datetime.today().year, date_val.month, date_val.day)


def next_week(date_val):
    start = datetime.today().date()

    if datetime.weekday(start) == 5:
        end = datetime.today().date() + dt.timedelta(days=6)
    elif datetime.weekday(start) == 6:
        end = datetime.today().date() + dt.timedelta(days=5)
    else:
        end = datetime.today().date() + dt.timedelta(days=7)
    return (date_val >= start) and (date_val <= end)


def shift(date_val):
    weekday = WEEKDAYS[datetime.weekday(helper(date_val))]
    if weekday in ["Saturday", "Sunday"]:
        weekday = "Monday"
    return weekday


def get_birthdays_per_week(users):
    birthdays = {u["name"]:shift(u["birthday"]) for u in users if next_week(helper(u["birthday"]))}
    #print(birthdays)
    for day in WEEKDAYS.values():
        user_names = ", ".join([u for u, d in birthdays.items() if d == day])
        if user_names:
            print(f"{day}: {user_names}")


if __name__ == '__main__':
    users = [{"name":"Ivan", "birthday": datetime.today().date() + dt.timedelta(days=6)},
             {"name":"Roman", "birthday": datetime.today().date() + dt.timedelta(days=16)},
             {"name":"Sahsa", "birthday": datetime.today().date() + dt.timedelta(days=2)},
             {"name":"Masha", "birthday": datetime.today().date() + dt.timedelta(days=3)},
             {"name":"Dasha", "birthday": datetime.today().date() + dt.timedelta(days=8)},
             {"name":"Pasha", "birthday": datetime.today().date() + dt.timedelta(days=-6)}]
    print(users)
    get_birthdays_per_week(users)
