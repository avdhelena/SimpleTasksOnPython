#todo
# Создайте декоратор, которые переводит все текстовые аргументы функции в верхний регистр и возвращает их в виде списка текстовых аргументов.
import itertools


def str_transform_decorator(func):
    def wrapper(*args, **kwargs):
        str_args = [arg.upper() for arg in itertools.chain(args, kwargs.values()) if type(arg) == str]
        print(f"Original arguments of {func.__name__}: ")
        print(args)
        print(kwargs.items())
        func(args, kwargs)
        return str_args
    return wrapper


@str_transform_decorator
def process_01(str_01, str_02):
    print("do process 01")


@str_transform_decorator
def process_02(str_01, str_02):
    print("do process 02")


args_list_01 = process_01("guests", 20, "presentation", 100, name_01="Nina", name_02="Maria")
args_list_02 = process_02(345.56, "sin", 10, "cos", action='addition', parameter='2456')

print("results:")
print(args_list_01)
print(args_list_02)
