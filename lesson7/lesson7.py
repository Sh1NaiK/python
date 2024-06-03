'''
1. Создать модуль `exceptions`, в нем класс `ValidationError`, который наследуется от `Exception`. Никакие методы,
   свойства переопределять не нужно, необходимо только описать в docstring, что это класс ошибки валидации данных.
2. Создать модуль `validator`, в котором:
    1. Реализовать класс `Data`, конструктор которого принимает `name` и `age` аргументы, сохраняет их в одноименные
       переменные экземпляра класса. Так же у этого класса должен быть метод `_clear_whitespaces`, который очищает от
       пробелов в на+-чале и в конце переменные `name` и `age` у экземпляра класса. Вызывать метод `_clear_whitespaces`
       необходимо из конструктора класса.
    2. Реализовать класс `DataWithDate`, наследовавшись от класса `Data`. Конструктор должен делать то же самое, что и
       родительский класс, но дополнительно сохраяняет текущее время, когда был создан этот экземпляр класса (
       см. `datetime.utcnow`).
    3. Реализовать класс `Validator`. У класса `Validator` должны быть следующие методы:
        1. конструктор класса — в экземпляре класса создает переменную `data_history`, которая является пустым списком,
           но будет хранить объекты класса `Data`.
        2. `_validate_name` — валидация имени (скопировать код из функции `validate_name`).
        3. `_validate_age` — валидация возраста (скопировать код из функции `validate_age`).
        4. `validate` — принимает аргумент `data` (объект класса `Data`) и сохраняет в список `data_history`. Далее
           запускает методы валидации, описанные выше.

       При этом методы `_validate_name` и `_validate_age` должны брать имя и возраст из
       переменной `Validator.data_history` (самое последнее значение). А также выбрасывать исключения `ValidationError`
       вместо `Exception`. Если переменная `data_history` пуста, тогда выбрасывать исключение `ValueError`.

3. В вашем основном файле, где вся текущая домашка:
    1. В самом верху необходимо импортировать класс `Validator` из модуля `validator`.
    2. В самом верху необходимо импортировать класс `ValidationError` из модуля `exceptions`.
    3. В функции `main` до цикла создать объект класса. Вызвать метод `validate` вместо тех функций валидаций, которые
       были написаны в домашках ранее - эти функции необходимо удалить из этого файла. Обрабатывать
       ошибку `ValidationError` вместо `Exception`.
    4. После того как пользователь ввел данные, необходимо создать объект класса `DataWithDate` и далее работать только
       с ним.
    5. Теперь количество попыток ввода данных должно выводиться только в том случае, если пользователь не смог с первого
       раза ввести верные данные. (А еще придумайте как можно избавиться от счетчика попыток).
    6. После ввода верных данных и до запуска игры необходимо показать пользователю:
       1. Общее количество попыток
       2. Время первой попытки, время последней попытки
       3. Сколько времени понадобилось пользователю, чтобы от первой попытки дойти к последней (формат HH:MM:SS, где HH
        - часы, MM - минуты, SS - секунды)

Примечания:
1. int(age) нужно сделать после очистки строки от пробелов в конструкторе класса
2. в экземпляре класса создает переменную data_history, которая является пустым списком,
но будет хранить объекты класса Data — это вам необходимо знать для того,
чтобы вы могли сделать type hint для этой переменной
3. Счетчик попыток оставить на месте как есть
4. Где вызывать ValueError
'''

from validator import Validator
from validator import Data
from validator import DataWithDate
from exceptions import ValidationError
import re
import random
from datetime import datetime


def advice(age) -> str | None:
    text = None
    if age == '16' or age == '17':
        text = ' Не забудь получить свой первый паспорт'
    elif age == '25' or age == '26':
        text = ' Не забудь заменить свой паспорт'
    elif age == '45' or age == '46':
        text = ' Не забудь заменить свой паспорт второй раз'
    return text


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
    text = None
    validator = Validator()
    time_list = []
    while text is None:

        name = input("Введите ваше имя: ").capitalize()
        age = input("Введите ваш возраст: ")
        try:
            data = Data(name, age)
            time_list.append(datetime.now())
            validator.validate(data)
        except ValidationError as ve:
            print(ve)
            continue
        except ValueError as val_err:
            print(val_err)
            continue
        data_with_date = DataWithDate(name, age)
        text = f'Привет, {data_with_date.name}! Тебе {data_with_date.age} лет.'
        advicee = advice(data_with_date.age)
        if advicee:
            text += advicee
        print(text)
    if len(time_list) > 1:
        time_count = time_list[len(time_list) - 1] - time_list[0]
        print(f'Общее количество попыток {len(time_list)}\n Время первой попытки {
            time_list[0]}\n Время последней попытки {time_list[len(time_list) - 1]}\n Времени понадобилось - {str(time_count).split(".")[0]}')
    else:
        print(f'Время попытки {time_list[0]}')
    random_number()


if __name__ == '__main__':
    main()
