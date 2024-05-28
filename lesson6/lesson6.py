'''
1)Сделать функцию is_palindrome, которая определяет является ли строка палиндромом или нет.
При этом введено может быть как слово, так и целые предложения с пробелами и с различными знаками препинания.
Необходимо избегать всех символов кроме букв.
А также не копировать входящие данные (например, развернуть строку через срез — это скопировать входящие данные)
2)Функции на проверку имени, возраста и совет паспорт должны возвращать None (иначе говоря, ничего не должны возвращать), если не было ошибок или нет советов
3)Сделать функцию, которая генерирует случайное число от 0 до 10, и в бесконечном цикле просит пользователя угадать это число, если пользователь ввёл имя и возраст корректные
'''

import re
import random


def name_verification(name):
    text = ""
    if not name:
        text = "Вы не ввели ваше имя!\n"
    elif len(name) <= 3:
        text = "Имя должно содердать больше 3 символов.\n"
    if name.count(" ") > 1:
        text = "Между буквами допускается только один пробел.\n"
    return text or None


def age_verification(age):
    text = ""
    if age.isnumeric():
        age = int(age)
        if age <= 0:
            text = "Некорректный возраст!\n"
        if age < 14:
            text = "Минимальный возраст 14 лет.\n"
    else:
        text = "Некорректный возраст!\n"
    return text or None


def cleaner(data):
    return data.strip(" ")


def advice(text, age):
    if age == '16' or age == '17':
        text += ', Не забудь получить свой первый паспорт'
    elif age == '25' or age == '26':
        text += ', Не забудь заменить свой паспорт'
    elif age == '45' or age == '46':
        text += ', Не забудь заменить свой паспорт второй раз'
    return text or None


def is_palindrome():
    word = re.sub(r'[^A-Za-zА-Яа-я]', '', input('Введите строку: '))
    i = 0
    j = len(word) - 1
    while (i < j):
        if word[i].lower() != word[j].lower():
            return False
        i += 1
        j -= 1
    return True


def random_number():
    rand_number = random.randint(0, 10)
    while True:
        choice = input("Введите число от 0 до 10: ")
        if (rand_number == int(choice)):
            print("Молодец")
            break
        else:
            print("Попробуй еще раз")


def main():
    text = "error"
    while text:
        name = cleaner(input("Введите ваше имя: ").capitalize())
        text = name_verification(name)
        if not text:
            age = cleaner(input("Введите ваш возраст: "))
            text = age_verification(age)
        if not text:
            text = f'Привет, {name}! Тебе {age} лет.'
            advicee = advice(text, age)
            if advicee != None:
                text += advicee
        print(text)
        if text.startswith("Привет"):
            break


main()
random_number()
