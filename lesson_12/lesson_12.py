# Створіть масив зі строками, які будуть складатися з чисел, які розділені комою. Наприклад: [”1,2,3,4”, ”1,2,3,4,50” ”qwerty1,2,3”]
# Для кожного елементу списку виведіть суму всіх чисел (створіть нову функцію для цього). Якщо є символи, що не є числами (”qwerty1,2,3” у прикладі)
# Вам потрібно зловити вийняток і вивести “Не можу це зробити!” Використовуйте блок try\except, щоб уникнути інших символів, окрім чисел у списку.
# Для цього прикладу правильний вивід буде - 10, 60, “Не можу це зробити”



def calculate_sum_of_numbers(string):
    try:
        numbers = map(int, string.split(','))
        return sum(numbers)
    except ValueError:
        return "Не можу це зробити!"

def process_list(strings):
    results = []
    for s in strings:
        result = calculate_sum_of_numbers(s)
        results.append(result)
    return results

strings = ["1,2,3,4", "1,2,3,4,50", "qwerty1,2,3"]
print(process_list(strings))
