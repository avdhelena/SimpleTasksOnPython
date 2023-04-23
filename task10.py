#Единицы массы пронумерованы следующим образом: 1 — килограмм, 2 — миллиграмм, 3 — грамм, 4 — тонна, 5 — центнер.
#Дан номер единицы массы и масса тела M в этих единицах (вещественное число). Вывести массу данного тела в килограммах.
# Данную задачу нужно решить с помощью конструкции  match  (Python v3.10)

# Пример:
# Введите единицу массы тела
#       1 - килограмм
#       2 — миллиграмм
#       3 — грамм
#       4 — тонна
#       5 — центнер
#>4

#Введите  массу тела
#>1

#Ответ: 1000 кг

measure = int(input("Enter measure number:"))
weight = int(input("Enter weight:"))
power = 0
match measure:
    case 1:
        power = 3
    case 2:
        power = -3
    case 3:
        power = 0
    case 4:
        power = 6
    case 5:
        power = 5
    case _:
        print("Wrong measure number!!!")
        power = 3


res = weight * (10**(power-3))
print(f"weight in kg: {res}")







