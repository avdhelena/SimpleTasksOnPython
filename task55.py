# #todo: Написать авторизацию пользователя в систему.
# При реализации авторизации спроектировать абстрактный класс и реализовать методы в наследуемом классе
# login, check_password, check_login

# При запуске программы пользователю необходимо ввести
# логин и пароль, поэтапно.
# login: _________
# password: ________
#
# При неправильном вводе логина должно генерироваться пользовательское исключение LoginNotFound
# Введеный пароль должен проверятся на длину. Длина должна быть более 8 символов иначе генерируем пользовательское
# исключение LengthError
# При вводе некорректного пароля генерируем соответсвуещее исключение
# При успешном заходе генерируем исключение "Доступ разрешен!"


from abc import ABC, abstractmethod


class LoginNotFound(Exception):
    pass


class LengthError(Exception):
    pass


class PasswordError(Exception):
    pass


class LoginPasswordConfirmed(Exception):
    pass


class AuthorizationABS(ABC):

    @abstractmethod
    def login(self):
        pass

    @ abstractmethod
    def check_login(self, login_name):
        pass

    @abstractmethod
    def check_password(self, password):
        pass


class Authorization(AuthorizationABS):

    def __init__(self):
        self.auth_login = None
        self.auth_password = None

    def login(self):
        val = input("login:")
        self.check_login(val)
        self.auth_login = val
        print(self.auth_login)
        val = input("password:")
        self.check_password(val)
        self.auth_password = val
        print(self.auth_password)
        raise LoginPasswordConfirmed("Доступ разрешен!")

    def check_login(self, login_name):
        if login_name not in ['Helena', 'Anna', 'Alex']:
            raise LoginNotFound(f"Логин {login_name} отсутствует в системе")

    def check_password(self, password):
        if len(password) < 9:
            raise LengthError('Длина пароля должна быть больше 8')
        if not password == '123456789':
            raise PasswordError('Неверный пароль')




auth = Authorization()

try:
    auth.login()
except (LoginNotFound, PasswordError, LengthError) as e:
    print("Ошибка авторизации: ",e)
except LoginPasswordConfirmed as e:
    print(e)



