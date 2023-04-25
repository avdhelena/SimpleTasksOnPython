# todo: Дан номер некоторого года (положительное целое число).
# Вывести соответствующий ему номер столетия, учитывая, что, к примеру, началом 20 столетия был 1901 год.

year = int(input("Enter year (four-digit number):"))

century = year // 100
if year % 100:
    century += 1
print(f"century {century}")


