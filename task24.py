#todo: Напишите программу, которая:
# Получает на вход две строки, в которых перечисляются книги, прочитанные двумя учениками.
# Выводит количество книг, которые прочитали оба ученика.
# Пример ввода:
# Война и мир, Над пропастью во ржи, Мастер и Маргарита, Идиот
# Евгений Онегин, Идиот, Мастер и Маргарита, Война и мир


books_01 = set(input("Enter books for first pupal:").split())
books_02 = set(input("Enter books for second pupal:").split())

print(f"Common books:{ books_01.intersection(books_02)}")