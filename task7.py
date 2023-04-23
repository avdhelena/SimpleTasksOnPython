# todo:  Даны три переменные: X, Y, Z. Их значения числа.
# Из данных произвольных чисел выбрать наибольшее.

# Пример:
# X = 5
# Y = 10
# Z = 3
# Ответ: Наибольшее число 10.
#
# X = 10
# Y = 12
# Z = -7
# Ответ: Наибольшее число 12.

x = int(input("Input X:"))
y = int(input("Input Y:"))
z = int(input("Input Z:"))

x = x if x > y else y
x = x if x > z else z
print(f"From x:{x} y:{y} z:{z}: Greatest: {x}")

