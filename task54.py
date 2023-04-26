# todo:
#  Функция get_weekday()
#  Реализуйте функцию get_weekday(), которая принимает один аргумент:
#
#  number — целое число (от 1 до 7 включительно)
#  Функция должна возвращать полное название дня недели на русском, который соответствует числу number, при этом:
#
#  если number не является целым числом, функция должна возбуждать исключение:
#  TypeError('Аргумент не является целым числом')
#  если number является целым числом, но не принадлежит отрезку [1;7]
#  функция должна возбуждать исключение:
#  ValueError('Аргумент не принадлежит требуемому диапазону')

#todo:
# Сделайте функцию get_weekday() статической в классе Helper

class Helper:

    @staticmethod
    def get_weekday(week_number):
        days = ['Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота', 'Воскресенье']

        if type(week_number) is not int:
            raise TypeError('Аргумент не является целым числом')
        if not (1 <= week_number < 8):
            raise ValueError('Аргумент не принадлежит требуемому диапазону')

        return days[week_number-1]


for week_day in [1, 2, 3, 4, 5, 6, 7, "jfdjf", 32]:
    try:
        wd = Helper.get_weekday(week_day)
    except (ValueError, TypeError) as e:
        print(f"Ошибка заданоного параметра ({week_day}): ", e)
    else:
        print(f"День недели ({week_day}): {wd}")

