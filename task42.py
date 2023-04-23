#todo:
# Создайте функцию-генератор, которая создает последовательность числовых
# палиндромов: 1 2 3 4 5 6 7 8 9 11 22 33 44 55 66 77 88 99 101 111 121 131 141 151 161 171 181 191 202 212 …

def generate_palindrome(limit):
    return list(filter(lambda x: str(x) == str(x)[-1::-1], range(1,limit+1)))


limit = int(input("Enter limit: "))
print(f"palindrome for limit {limit}: {generate_palindrome(limit)}")
