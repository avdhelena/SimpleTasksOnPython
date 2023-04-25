#todo:
# Каждый третий четверг каждого месяца билеты в Эрмитаж бесплатны.
# Напечатайте список дат в 2023 году, когда вход бесплатен.

import calendar

first_days = list(map(lambda month: calendar.monthrange(2023, month)[0], range(1, 13)))

free_thursdays = []
for month in range(1, 13):
    first_day = first_days[month-1]
    thursday = 1 + 14 + 3 - first_day if first_day <= 3 else 1 + 14 + 3 + (7 - first_day)
    free_thursdays.append(f"{thursday}.{month}.2023")

print(", ".join(free_thursdays))