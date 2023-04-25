#todo: Напишите функцию, которая шифрует строку, содержащую латинские буквы с помощью шифра Цезаря.
# Каждая буква сдвигается на заданное число n позиций вправо. Пробелы, знаки препинания не меняются. Например, для n = 1.
# a → b,   b → c,    p → q,    y → z,    z V a
# A → B,   B → C,   Z → A
# Т.е. заголовок функции будет def code(string, n):
# В качестве результата печатается сдвинутая строка.

def code(string, n):
    result_string = [chr(ord(s)+n) if s.isalpha() else s for s in string]
    return ''.join(result_string)


source_str = input("Enter sentence: ")
N = int(input("Enter number: "))
print(f"source string: {source_str}")

encoded_string = code(source_str, N)
print(f"encoded_string: {encoded_string}")




