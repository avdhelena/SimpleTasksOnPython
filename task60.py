# Назовем пароль хорошим, если
#
# его длина равна 9 или более символам
# в нем присутствуют большие и маленькие буквы любого алфавита
# в нем имеется хотя бы одна цифра
# Напишите программу, которая требует ввода нового пароля до тех пор, пока не будет введен хороший.
#
#
# На вход программе подается произвольное количество паролей, каждый на отдельной строке. Гарантируется, что среди них присутствует хороший.
#
#
# Для каждого введенного пароля программа должна вывести текст:
#
# LengthError, если длина введенного пароля меньше 9 символов
# LetterError, если в нем все буквы имеют одинаковый регистр
# DigitError, если в нем нет ни одной цифры
# Success!, если введенный пароль хороший
#
# После ввода хорошего пароля все последующие пароли должны игнорироваться.
# Примечание 1. Приоритет вывода сообщений об ошибке в случае невыполнения нескольких условий:
# LengthError, затем LetterError, а уже после DigitError.
#
#
# Sample Input 1:
#
# arr1
# Arrrrrrrrrrr
# arrrrrrrrrrrrrrr1
# Arrrrrrr1
# Sample Output 1:
#
# LengthError
# DigitError
# LetterError
# Success!
#
# Sample Input 2:
#
# beegeek
# Beegeek123
# Beegeek2022
# Beegeek2023
# Beegeek2024
# Sample Output 2:
# LengthError
# Success!

import os
import sys
import logging
from argparse import ArgumentParser

version = "1.0.1"
parser = ArgumentParser(description='Выбор подходящего пароля.')
parser.add_argument("-v", "--version", action="version", version=version)
parser.add_argument("--debug", action="store_true", help="enable debug mode")
parser.add_argument('passwords', metavar='N', type=str, nargs='+',
                    help='Список паролей для поиска подходящего')


class ExceptionPasswordLengthError(Exception):
    pass


class ExceptionPasswordLetterError(Exception):
    pass


class ExceptionPasswordDigitError(Exception):
    pass


class ExceptionPasswordSuccess(Exception):
    pass


if __name__ == "__main__":
    args = parser.parse_args()
    prog_name = os.path.splitext(parser.prog)[0]
    logger = logging.getLogger()
    logger.name = prog_name
    handler = logging.StreamHandler()
    formatter = logging.Formatter('%(levelname)s %(name)s - %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    if args.debug:
        logger.setLevel(logging.DEBUG)
    else:
        logger.setLevel(logging.INFO)

    passwords = list(args.passwords)
    wait_for_correct_password = True
    while wait_for_correct_password:
        logger.debug(f"Поиск корректного пароля: {passwords}\n")

        for password in passwords:
            logger.debug(f"password: \t{password}")
            try:
                if len(password) < 9:
                    raise ExceptionPasswordLengthError(f"Пароль {password} задан неверно:: длина пароля меньше 9")

                letters = ''.join([letter for letter in password if letter.isalpha()])
                if letters.islower() or letters.isupper():
                    raise ExceptionPasswordLetterError(f"Пароль {password} задан неверно: все буквы имеют одинаковый регистр")

                if not len(letters):
                    raise ExceptionPasswordLetterError(f"Пароль {password} задан неверно: отсутствуют буквы")

                for digit in range(1, 10):
                    if str(digit) in password:
                        break
                else:
                    raise ExceptionPasswordDigitError(f"Пароль {password} задан неверно: нет ни одной цифры")

                raise ExceptionPasswordSuccess(f"Пароль {password} задан корректно!")

            except (ExceptionPasswordLengthError, ExceptionPasswordLetterError,
                    ExceptionPasswordDigitError) as exc:
                logger.error(exc)
            except ExceptionPasswordSuccess as exc:
                logger.info(exc)
                wait_for_correct_password = False
                break

        if wait_for_correct_password is True:
            passwords = input("\nВведите корректный пароль: ").split()
        else:
            break
