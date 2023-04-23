# todo: На вход подается список, состоящий из списков чисел, например: [[1,5,3], [2,44,1,4], [3,3]].
#  Отсортируйте этот список по возрастанию общего количества цифр в каждом списке.
#  Каждый список отсортируйте по убыванию.

source_list = [[1,5,3], [2,44,1,4], [3,3]]
print(f"source list: {source_list}")
for lst in source_list:
    lst.sort(reverse=True)
sorted_list = sorted(source_list,key=len)

print(f"sorted list: {sorted_list}")