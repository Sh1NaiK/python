'''
1. В файл сохранять теперь данные в формате json
2. Разобраться как сериализовать datetime в json (Гугл, а потом написать подробно в комменте почему именно так)
3. *Написать класс валидатора, написать валидацию для пароля:
минимум 4 символа, минимум один заглавный символ, минимум один прописной символ, минимум одна цифра, минимум один спецсимвол.
Хэшировать пароль любым алгоритмом на выбор, обосновать в комменте выбор алгоритма (можно хоть свой сделать).
Написать метод валидации почты. Вместо логина у вас должен быть ввод почтового адреса.
'''

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


def registration(authenticator):
    print("Необходимо зарегестрироваться")
    login = input("Введите логин: ")
    password = input("Введите пароль: ")
    authenticator.registrate(login, password)


def main():
    authenticator = Authenticator()
    while True:
        if authenticator.login != None:
            print("Необходимо авторизоваться")
            login = input("Введите логин: ")
            password = input("Введите пароль: ")
            authenticator.authorize(login, password)
            break
        else:
            registration(authenticator)
    print(f'Здравствуйте {authenticator.login}, время последней успешной авторизации {
        str(authenticator.last_success_login_at).split(".")[0]}, неудачных попыток входа {authenticator.errors_count}')
    random_number()


if __name__ == '__main__':
    main()
