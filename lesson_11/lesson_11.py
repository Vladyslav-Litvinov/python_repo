# # task 1
# """ Задача - надрукувати табличку множення на задане число, але
# лише до максимального значення для добутку - 25.
# Код майже готовий, треба знайти помилки та випраавити\доповнити.
# """
# def multiplication_table(number):
#     # Initialize the appropriate variable
#     multiplier = 1
#
#     # Complete the while loop condition.
#     while multiplier <= number:
#         result = number * multiplier
#         # десь тут помилка, а може не одна
#         if  result > "25":
#             # Enter the action to take if the result is greater than 25
#             pass
#         print(str(number) + "x" + str(multiplier) + "=" + str(result))
#
#         # Increment the appropriate variable
#         multi += 1
#
# multiplication_table(3)
# # Should print:
# # 3x1=3
# # 3x2=6
# # 3x3=9
# # 3x4=12
# # 3x5=15
#
#
# # task 2
# """  Написати функцію, яка обчислює суму двох чисел.
# """
#
#
# # task 3
# """  Написати функцію, яка розрахує середнє арифметичне списку чисел.
# """
#
# # task 4
# """  Написати функцію, яка приймає рядок та повертає його у зворотному порядку.
# """
#
# # task 5
# """  Написати функцію, яка приймає список слів та повертає найдовше слово у списку.
# """
#
# # task 6
# """  Написати функцію, яка приймає два рядки та повертає індекс першого входження другого рядка
# у перший рядок, якщо другий рядок є підрядком першого рядка, та -1, якщо другий рядок
# не є підрядком першого рядка."""
# def find_substring(str1, str2):
#
#     return -1
#
# str1 = "Hello, world!"
# str2 = "world"
# print(find_substring(str1, str2)) # поверне 7
#
# str1 = "The quick brown fox jumps over the lazy dog"
# str2 = "cat"
# print(find_substring(str1, str2)) # поверне -1
#
# # task 7
# # task 8
# # task 9
# # task 10
# """  Оберіть будь-які 4 таски з попередніх домашніх робіт та
# перетворіть їх у 4 функції, що отримують значення та повертають результат.
# Обоязково документуйте функції та дайте зрозумілі імена змінним.
# """

# task 1
def multiplication_table(number):
    multiplier = 1
    while True:
        result = number * multiplier
        if result > 25:  # Порівняння з числом
            break
        print(str(number) + "x" + str(multiplier) + "=" + str(result))
        multiplier += 1

multiplication_table(3)

# task 2
def add_numbers(a, b):
    return a + b

# task 3
def calculate_average(numbers):
    return sum(numbers) / len(numbers)

# task 4
def reverse_string(s):
    return s[::-1]

# task 5
def find_longest_word(words):
    return max(words, key=len)

# task 6
def find_substring(str1, str2):
    return str1.find(str2)

str1 = "Hello, world!"
str2 = "world"
print(find_substring(str1, str2))

str1 = "The quick brown fox jumps over the lazy dog"
str2 = "cat"
print(find_substring(str1, str2))

# task 7
def sum_even_numbers(numbers_list):
  sum_even = 0
  for num in numbers_list:
    if num % 2 == 0:
      sum_even += num
  return sum_even
# task 8
def filter_strings(data_list):
  string_list = []
  for item in data_list:
    if isinstance(item, str):
      string_list.append(item)
  return string_list
# task 9
def check_for_h(word):
  return 'h' in word.lower()
while True:
  user_word = input("Введіть слово, яке містить літеру 'h': ")
  if check_for_h(user_word):
    print("Вітаю! Ви ввели слово з літерою 'h'.")
    break
  else:
    print("Слово не містить літеру 'h'. Спробуйте ще раз.")
# task 10
areas = [434402, 37800]
total_area = 0
for area in areas:
    total_area += area
print("Сумарна площа Чорного та Азовського морів:", total_area, "км2")