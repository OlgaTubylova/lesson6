# В модуль с проверкой даты добавьте возможность запуска в терминале с передачей даты на проверку.

import argparse

def _is_leap_year(year):
    """Проверяет, является ли год високосным"""
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)


def is_date_valid(date):
    """Проверяет, существует ли введённая дата"""
    try:
        day, month, year = map(int, date.split('.'))
    except ValueError:
        return False  # Если ввод не число или неверный формат

    if not (1 <= year <= 9999):
        return False  # Год выходит за допустимые пределы
    if not (1 <= month <= 12):
        return False  # Некорректный месяц
    if day < 1:
        return False  # Некорректный день

    # Количество дней в каждом месяце
    days_in_month = {1: 31, 2: 29 if _is_leap_year(year) else 28,
                     3: 31, 4: 30, 5: 31, 6: 30,
                     7: 31, 8: 31, 9: 30, 10: 31,
                     11: 30, 12: 31}

    return day <= days_in_month[month]


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Проверка корректности даты")
    parser.add_argument("date", type=str, help="Дата в формате DD.MM.YYYY")
    args = parser.parse_args()

    if is_date_valid(args.date):
        print("Дата корректна")
    else:
        print("Дата некорректна")
