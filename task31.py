#todo: Дан список из кортежей (Фамилия, премия). Напечатать эти кортежи в порядке убывания премии.
# Тех, у кого одинаковая премия, то печатать в алфавитном порядке.
#  Пример ввода:
# [(Иванов, 100), (Петров, 200), (Сидоров, 200), (Воробьев, 100), (Лунин, 200)]
# Вывод:
#     Лунин 200
#     Петров 200
#     Сидоров 200
#     Воробьев 100
#     Иванов 100
#
#     Примечание:
#     https://pythonist.ru/lyambda-funkczii-dlya-sortirovki-razlichnyh-spiskov-v-python/

reward_list = [('Иванов', 100), ('Петров', 200), ('Сидоров', 200), ('Воробьев', 100), ('Лунин', 200),('Болдов', 200)]
print(reward_list)
reward_list.sort()
print(reward_list)
reward_list.sort(key = lambda element : element[-1],reverse=True)
print(reward_list)
