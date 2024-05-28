'''
# Домашнее задание
## Задание
Берём уже то, что вы сделали к последнему уроку.
0. Обязательно к прочтению Дзен python.
1. Создать несколько функций на проверку введённых данных:
- Проверка имени
- Проверка возраста Функции должны возвращать строку с ошибкой. Если функции вернули ошибки, нужно вывести
пользователю ошибки.
2. Улучшить проверку имени: в имени между буквами допускается только 1 пробел.
3. Сделать совет по получению или замене паспорта (эта задача больше не является со звездочкой) в отдельной функции,
которая возвращает строку.
4. Создать функцию main, в которой будут вызовы всех остальных функций, ввод данных и прочее.
5. Создать цикл до тех пор, пока пользователь не введёт верные данные без ошибок.
6. Создать функцию, которая очищает введённые данные от лишних пробелов в начале и в конце строки.
### Ограничения:
- Разрешается использовать только два раза print.
- Нельзя использовать глобальные переменные
### Дополнительная информация:
- Когда вы упакуете весь код в функции и запустите приложение, то у вас не будет запрошено что-то ввести и вывода тоже
не будет. Рекомендую сначала вам дойти до этого момента, столкнуться с этой проблемой, 10 раз подумать, вспомнить
прошлый урок.
'''


def name_verification(name):
    text = ""
    if not name:
        text = "Вы не ввели ваше имя!\n"
    elif len(name) <= 3:
        text = "Имя должно содердать больше 3 символов.\n"
    if name.count(" ") > 1:
        text = "Между буквами допускается только один пробел.\n"
    return text


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
    return text


def cleaner(data):
    return data.strip(" ")


def advice(name, age):
    text = f'Привет, {name}! Тебе {age} лет.'

    if age == '16' or age == '17':
        text += ', Не забудь получить свой первый паспорт'
    elif age == '25' or age == '26':
        text += ', Не забудь заменить свой паспорт'
    elif age == '45' or age == '46':
        text += ', Не забудь заменить свой паспорт второй раз'
    return text


def main():
    text = "error"
    while text:
        name = cleaner(input("Введите ваше имя: ").capitalize())
        text = name_verification(name)
        age = cleaner(input("Введите ваш возраст: "))
        text += age_verification(age)
        if not text:
            text = advice(name, age)
        print(text)
        if text.startswith("Привет"):
            break


main()
