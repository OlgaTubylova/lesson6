# Напишите функцию в шахматный модуль. Используйте генератор случайных чисел для случайной расстановки ферзей в задаче выше. Проверяйте различный случайные варианты и выведите 4 успешных расстановки.

import random

def is_safe_queens(queens):
    for i in range(8):
        for j in range(i + 1, 8):
            x1, y1 = queens[i]
            x2, y2 = queens[j]
            
            if x1 == x2 or y1 == y2 or abs(x1 - x2) == abs(y1 - y2):
                return False  # Ферзи бьют друг друга
    return True  # Ферзи не бьют друг друга

def generate_random_queens():
    successful_positions = []
    
    while len(successful_positions) < 4:
        queens = [(i + 1, random.randint(1, 8)) for i in range(8)]
        if is_safe_queens(queens):
            successful_positions.append(queens)
    
    return successful_positions

# Вывод 4 успешных расстановок
for idx, positions in enumerate(generate_random_queens(), 1):
    print(f"Успешная расстановка {idx}: {positions}")
