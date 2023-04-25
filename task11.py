#todo: Дан целочисленный массив размера N из 10 элементов.
#Преобразовать массив, увеличить каждый его элемент на единицу.

data = [23,14,-35,76,787,48,29,134,34,14]
print(f"data at begin: {data}")
for i in range(len(data)):
    data[i] = data[i] + 1
print(f"data modified + 1: {data}")

data = [x+1 for x in data]
print(f"data modified + 1: {data}")


