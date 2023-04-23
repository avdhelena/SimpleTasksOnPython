#todo:  Напишите программу, которая получает на вход строку, и определяет,
# является ли строка панграммой (т.е. содержатся ли в ней все 33 буквы русского алфавита).

# Подъём с затонувшего эсминца легкобьющейся древнегреческой амфоры сопряжён с техническими трудностями.

tested_str = set(ord(s.lower()) for s in input("Enter sentence: ") if s.isalpha())
print(f"source string: {sorted(tested_str)}")

pattern_str = set(l for l in range(ord('а'),ord('я')+1))
pattern_str.add(ord('ё'))
print(f"pattern string: {sorted(pattern_str)}")
print(f"String is { '' if tested_str == pattern_str else 'not ' }pangram")