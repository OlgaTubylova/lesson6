# Создайте модуль с функцией внутри. Функция принимает на вход три целых числа: нижнюю и верхнюю границу и количество попыток. Внутри генерируется случайное число в указанных границах и пользователь должен угадать его за заданное число попыток. Функция выводит подсказки “больше” и “меньше”. Если число угадано, возвращается истина, а если попытки исчерпаны - ложь.

from random import randint

def guess_number(lower_limit, upper_limit, count):
    """Функция угадывания числа"""
    n = randint(lower_limit, upper_limit)
    print(f"Компьютер загадал число. Отгадайте его за {count} попыток.")

    for i in range(1, count + 1):
        try:
            u = int(input(f"{i}-я попытка: "))
        except ValueError:
            print("Ошибка! Введите целое число.")
            continue

        if u > n:
            print("Меньше")
        elif u < n:
            print("Больше")
        else:
            print(f"Поздравляю! Вы угадали с {i}-й попытки!")
            return True  # Возвращаем истину при угаданном числе

    print(f"Вы проиграли. Было загадано число {n}.")
    return False  # Если попытки исчерпаны

if __name__ == '__main__':
    try:
        lower_limit = int(input("Введите нижнюю границу: "))
        upper_limit = int(input("Введите верхнюю границу: "))
        count = int(input("Введите количество попыток: "))

        if lower_limit >= upper_limit:
            print("Ошибка: нижняя граница должна быть меньше верхней.")
        elif count <= 0:
            print("Ошибка: количество попыток должно быть положительным числом.")
        else:
            guess_number(lower_limit, upper_limit, count)

    except ValueError:
        print("Ошибка ввода! Введите целые числа.")
