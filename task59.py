# todo: Десериализация
# Напишите программу, которая принимает на вход название JSON файла, десериализует содержащийся в этом файле объект и выводит его.
# если файла с данным названием нет в папке с программой, программа должна вывести текст:
# Файл не найден
# если файл с данным названием содержит некорректные данные (то есть не удовлетворяющие формату JSON), программа должна вывести текст:
# Ошибка при десериализации
#
# На вход программе подается название JSON файла.
#
#
# Программа должна десериализовать объект, содержащийся в файле с введенным названием, и вывести его.
# Если при поиске файла или десериализации его содержимого произошла ошибка, программа должна вывести соответствующий текст.
#
# Примечание 1. Название подаваемого файла уже содержит расширение.
#
# Примечание 2. Тестируемый файл numbers.json имеет следующее содержание
#
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# numbers.json
# Sample Output 1:
#
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

#
# Ошибка при десериализации
import os
import json
from argparse import ArgumentParser
import logging


version = "1.0.1"
parser = ArgumentParser(description='загрузка данных из файла в формате json')
parser.add_argument("-v", "--version", action="version", version=version)
parser.add_argument("--debug", action="store_true", help="enable debug mode")
parser.add_argument('input', help="Входной файл в формате json")  # positional argument

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

    logger.debug(f"Аргументны командной строки: {args}")

    json_object = None
    json_file_name = args.input
    logger.info(f"Чтение json-файла: {json_file_name}")
    try:
        with open(json_file_name, 'rt') as f:
            try:
                json_object = json.load(f)
                logger.info(f"Загружен json-объект: {json_object}")
            except ValueError:
                logger.fatal("Ошибка при десериализации " + json_file_name)

    except FileNotFoundError:
        logger.critical(f"Файл {json_file_name} не найден!")

    logger.info(f"Обработка файла {json_file_name} завершена!!!")