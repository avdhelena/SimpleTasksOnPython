# todo: Необходимо реализовать консольную утилиту marge.py которая реализует функцию слияния
# содержимого файлов определенного типа с указанного каталога в один файл json при задании параметров:
# ./ marge.py -v --root_dir=ROOT_FOLDER output.json
import os
import sys
import json
import logging
from argparse import ArgumentParser

version = "1.0.1"
parser = ArgumentParser(description='Сбор данных из файлов формата txt в выходной файл формата json')
parser.add_argument("-v", "--version", action="version", version=version)
parser.add_argument("--debug", action="store_true", help="enable debug mode")
parser.add_argument("--root_dir", help="Принимает папку для обработки", default='.')
parser.add_argument('output', help="Выходной файл в формате json")  # positional argument


def find_files(catalog, logger):
    data_files = []
    for root_dir, dirs, cur_files in os.walk(catalog):
        logger.debug(fr"Вход в папку: {root_dir}")
        data_files += [os.path.join(root_dir, file_name) for file_name in cur_files]
    return data_files


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

    files = find_files(args.root_dir, logger)

    logger.info("Запуск процесса сбора данных!!!")
    logger.info(f"Аргументы командной строки: {args}")
    logger.info(f"Список обрабытываемых файлов: {files}")

    VectorTelemetry = {}
    for path in files:
        name = os.path.basename(path)
        if '.' in name:
            name = os.path.splitext(name)[0]

        try:
            with open(path, 'r') as file:
                for line in file:
                    VectorTelemetry[name] = line
                    logger.debug(f"{name}: \t{line}")
        except FileNotFoundError:
            logger.critical(f"Файл {path} не найден")

    try:
        with open(args.output, 'wt') as file_out:
            json.dump({"VectorTelemetry": VectorTelemetry}, file_out,indent=4)
    except FileNotFoundError:
        logger.critical(f"Файл {args.output} не найден")

    logger.info("Успешное завершение процесса сбора данных!!!")
