'''
Программа, которая
- Запрашивает у пользователя имя и возраст;
- Проверяет минимальный возраст 14;
- Проверяет имя на пустоту;
- Проверяет возраст на отрицательное число или 0;
- Проверяет, что имя введено и минимальное количество символов в имени — 3;
* Проверяет, что возраст 16-17 лет и нужно не забыть получить первый паспорт;
    возраст 25-26 лет и нужно заменить паспорт; 
    возраст 45-46 лет и нужно второй раз заменить паспорт;
- Выводит либо текст с ошибкой, либо приветствие пользователя с его именем (с заглавной буквы), 
    указанием возраста и *советом получить/заменить паспорт (если совет актуален).
* Совет с паспортом выводить только в том случае, если отображается приветствие.

Ограничения:
- только один раз можно использовать print


Дополнительная информация, которая может вам пригодиться:
- Можно писать на русском языке текст внутри строк.
- Внутри блока кода в ветвлениях if-elif-else возможно писать еще if-elif-else.
'''

name = input("Введите ваше имя: ").capitalize()
text = ""
age = input("Введите ваш возраст: ")
if age.isnumeric():
    age = int(age)
else:
    text += "Некорректный возраст!\n"


def exceptions(name, age, text):
    if not name:
        text += "Вы не ввели ваше имя!\n"
    elif len(name) <= 3:
        text += "Имя должно содердать больше 3 символов.\n"

    if not text:
        if age <= 0:
            text += "Некорректный возраст!\n"
        elif age < 14:
            text += "Минимальный возраст 14 лет.\n"

    if not text:
        text = f'Привет, {name}! Тебе {age} лет.'

        if age == 16 or age == 17:
            text += ', Не забудь получить свой первый паспорт'
        elif age == 25 or age == 26:
            text += ', Не забудь заменить свой паспорт'
        elif age == 45 or age == 46:
            text += ', Не забудь заменить свой паспорт второй раз'
    return text


print(exceptions(name, age, text))
