# todo: Создайте функцию, которая принимает два аргумента, год и месяц, и возвращает list comprehension,
# содержащий все даты этого месяца в этом году. Используйте функцию monthrange(year, month) из модуля
# calendar для нахождения числа дней в месяце.
import calendar

def date_list(year,month):
    fist,days_in_month = calendar.monthrange(year, month)
    return [d for d in range(1,days_in_month+1)]


val_year, val_month = map(int,input("Enter year and month: ").split())
print(f" days in {val_month} {val_year}: {date_list(val_year,val_month)}")
