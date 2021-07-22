import datetime as dt


def generate_year_range(start_y : int = 2005, end_y : int = 2020) -> int:
    date_range = []
    for y in range(start_y, end_y+1):
        date_range.append([ dt.datetime.strftime( dt.datetime(y,1,1), "%Y-%m-%d"), dt.datetime.strftime( dt.datetime(y,12,31), "%Y-%m-%d")])
    return date_range