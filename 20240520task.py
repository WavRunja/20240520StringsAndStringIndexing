# Записываем строку в переменную example
example = "Тапинамбур"

# Выводим на экран первый символ строки
print(example[0])

# Выводим на экран последний символ строки (используя отрицательный индекс)
print(example[-1])

# Выводим на экран вторую половину строки (для строки с нечётным количеством символов)
# Для примера используем строку с нечётным количеством символов
example_odd = "Тапинамбур"
middle_index = len(example_odd) // 2
second_half = example_odd[middle_index:]
print(second_half)

# Выводим на экран строку наоборот
reversed_example = example[::-1]
print(reversed_example)

# Выводим на экран каждый второй символ строки
every_second_char = example[1::2]
print(every_second_char)

#Вывод на экран(в консоль):
#Т
#р
#амбур
#рубманилаТ
#аиабр