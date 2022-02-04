from datetime import datetime
import datetime as dt

def helper(date_val):
    return dt.date(datetime.today().year, date_val.month, date_val.day)

def next_week(date_val):
    start = datetime.today().date()
    end = datetime.today().date() + dt.timedelta(days=7)
    return (date_val >= start) and (date_val <= end)


def get_birthdays_per_week(users):
    weekdays = {0:"Monday", 1:"Tuesday", 2:"Wednesday", 3:"Thursday", 4:"Friday", 5:"Saturday", 6:"Sunday"}
    birthdays = {u["name"]:weekdays[datetime.weekday(helper(u["birthday"]))]
                 for u in users
                 if next_week(helper(u["birthday"]))}

    print(birthdays)



if __name__ == '__main__':
    users = [{"name":"Ivan", "birthday": dt.date(1980, 2, 9)},
             {"name":"Roman", "birthday": dt.date(1980, 2, 6)},
             {"name":"Sahsa", "birthday": dt.date(1980, 2, 5)},
             {"name":"Masha", "birthday": dt.date(1980, 2, 8)},
             {"name":"Dasha", "birthday": dt.date(1980, 3, 8)},
             {"name":"Pasha", "birthday": dt.date(1980, 1, 8)}]

    get_birthdays_per_week(users)
