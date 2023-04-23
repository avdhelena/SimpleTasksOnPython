# todo: Проверить истинность высказывания:
# "Данное четырехзначное число читается одинаково
# слева направо и справа налево".

val = input("Enter four-digit number:")
print(f"val[:2]{val[:2]}")
print(f"val[-1:-3:-1]{val[-1:-3:-1]}")


if val[:2] == val[-1:-3:-1]:
    print(f"{val} is a symmetric number")
else:
    print(f"{val} is a asymmetric number")