# todo: Ввод: 2 слова, разделенных пробелами. Для ввода используем функцию s = input().split()
#  Определить, являются ли эти слова анаграммами (словами с одинаковым набором букв). Если да, то True. Если нет, то False.
#  (Примеры: АКВАРЕЛИСТ-КАВАЛЕРИСТ, АНТИМОНИЯ-АНТИНОМИЯ, АНАКОНДА-КАНОНАДА, ВЕРНОСТЬ-РЕВНОСТЬ, ВЛАДЕНИЕ-ДАВЛЕНИЕ, ЛЕПЕСТОК-ТЕЛЕСКОП)

Word_01, Word_02 = map(str, input("Enter rwo words: ").split())

dict_01 = {}
for letter in Word_01:
    dict_01[letter] = dict_01[letter] + 1 if (letter in dict_01) else 1
dict_02 = {}
for letter in Word_02:
    dict_02[letter] = dict_02[letter] + 1 if (letter in dict_02) else 1

print(dict_01)
print(dict_02)
if dict_01 == dict_02:
    print(f"Words {Word_01} and {Word_02} are anagrams")
