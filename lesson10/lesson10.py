from authenticator import Authenticator
import random


def random_number():
    rand_number = random.randint(0, 10)
    while True:
        choice = input("Введите число от 0 до 10: ")
        if (rand_number == int(choice)):
            print("Молодец")
            break
        else:
            print("Попробуй еще раз")


def decor(func):
    def wrapper(*args, **kwargs):
        while func:
            func(*args, **kwargs)
    return wrapper


@decor
def main() -> bool:
    authenticator = Authenticator()
    while True:
        if authenticator.login != None:
            print("Необходимо авторизоваться")
            login = input("Введите логин:")
            password = input("Введите пароль:")
            authenticator.authorize(login, password)
            break
        else:
            print("Необходимо зарегестрироваться")
            login = input("Введите логин:")
            password = input("Введите пароль:")
            authenticator.registrate(login, password)
    print(f'Здравствуйте {authenticator.login}, время последней успешной авторизации {
        str(authenticator.last_success_login_at).split(".")[0]}, неудачных попыток входа {authenticator.errors_count}')
    return True


if __name__ == '__main__':
    main()
