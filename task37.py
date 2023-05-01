#todo: Реализовать декоратор в котором нужно подсчитать кол-во вызовов декорированной функции в процессе выполнения кода.
# Выгрузить статистику подсчета в файл debug.log в формате: Название функции, кол-во вызовов, дата-время последнего выполнения
# Пример:
# render, 10,  12.05.2022 12:00
# show,    5,  12.05.2022 12:02
# render, 15,  12.05.2022 12:07
#
# Декоратор должен применяться для различных функций с переменным числом аргументов.
# Статистику вызовов необходимо записывать в файл при каждом запуске скрипта.

from datetime import datetime

statistics_data = {}


def execution_counter(func):
    execution_count = 0

    def wrapper(*args, **kwargs):
        nonlocal execution_count
        global statistics_data
        func(*args, **kwargs)
        execution_count += 1
        curd = datetime.now()
        scurd = f"{curd.day}.{curd.month}.{curd.year} {curd.hour}:{curd.minute}"
        statistics_data[f"{func.__name__}"] = [execution_count, scurd]
        print(f"count of {func.__name__}() : {execution_count}")
    return wrapper


@execution_counter
def process_01(limit):
    res = [x**3 for x in range(limit) if x % 5 == 0]
    #print(f"result of processing: {res}")


@execution_counter
def process_02(limit):
    res = [x**3 for x in range(limit) if x % 5 == 0]
    #print(f"result of processing: {res}")


print(datetime.now())
process_01(10)
process_01(100)
process_02(5)
process_01(30)
process_02(45)

print(statistics_data)

fd = open("debug.log", "at")
for key, value in statistics_data.items():
    fd.writelines(f" {key}\t{value[0]},\t{value[1]}")
    fd.writelines(f"\n")
fd.close()

