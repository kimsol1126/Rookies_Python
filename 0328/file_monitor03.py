from datetime import date, timedelta

start_date = date(2023, 3, 1)
delta = timedelta(days=30)
end_date = start_date + delta

print(end_date)