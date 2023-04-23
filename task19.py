#todo: Напишите калькулятор (простой). На вход подается строка, например:
# 1 + 2  или  5 – 3  или  3 * 4  или  10 / 2.
# Вывод: сосчитать и напечатать результат операции.
# Гарантируется, что два операнда и операция есть в каждой строчке, и все они разделены пробелами.

str_a,operation,str_b = map(str,input("Enter mathematical expression:").split())
res = None
is_success = True
a = int(str_a)
b = int(str_b)
match operation:
    case '+': res = a + b
    case '-': res = a - b
    case '*': res = a * b
    case '/': res = a / b
    case '%': res = a % b
    case '//': res = a // b
    case _:
        print(f"Wrong operation {operation}")
        is_success = False

if is_success:
    print(f"{a} {operation} {b} = {res}")
