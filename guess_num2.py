# Улучшаем задачу 2. Добавьте возможность запуска функции “угадайки” из модуля в командной строке терминала. Строка должна принимать от 1 до 3 аргументов: параметры вызова функции. Для преобразования строковых аргументов командной строки в числовые параметры используйте генераторное выражение.

import sys
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

def main():
    """Обработчик командной строки"""
    try:
        # Преобразуем аргументы в числа с помощью генератора
        args = [int(arg) for arg in sys.argv[1:4]]

        # Разбираем параметры (по умолчанию: 1–100, 5 попыток)
        lower_limit = args[0] if len(args) > 0 else 1
        upper_limit = args[1] if len(args) > 1 else 100
        count = args[2] if len(args) > 2 else 5

        # Проверяем корректность границ
        if lower_limit >= upper_limit:
            print("Ошибка: нижняя граница должна быть меньше верхней.")
            return
        if count <= 0:
            print("Ошибка: количество попыток должно быть положительным числом.")
            return

        # Запускаем игру
        guess_number(lower_limit, upper_limit, count)

    except ValueError:
        print("Ошибка! Аргументы должны быть целыми числами.")

if __name__ == '__main__':
    main()
