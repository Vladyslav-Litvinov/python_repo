# ДЗ 1
def calculate_sum_of_numbers(string):
    try:
        numbers = map(int, string.split(','))
        return sum(numbers)
    except ValueError:
        return "Не можу це зробити!"
# ДЗ 2
def process_list(strings):
    results = []
    for s in strings:
        result = calculate_sum_of_numbers(s)
        results.append(result)
    return results

# ДЗ 3
def multiplication_table(number):
    table = []
    multiplier = 1
    while True:
        result = number * multiplier
        if result > 25:
            break
        table.append(f"{number}x{multiplier}={result}")
        multiplier += 1
    return table

# ДЗ 4
def sum_even_numbers(numbers_list):
    sum_even = 0
    for num in numbers_list:
        if num % 2 == 0:
            sum_even += num
    return sum_even

# Тести
def test_calculate_sum_of_numbers():
    assert calculate_sum_of_numbers("1,2,3,4") == 10
    assert calculate_sum_of_numbers("1,2,3,4,50") == 60
    assert calculate_sum_of_numbers("qwerty1,2,3") == "Не можу це зробити!"
    print("test_calculate_sum_of_numbers passed")

def test_process_list():
    assert process_list(["1,2,3,4", "1,2,3,4,50", "qwerty1,2,3"]) == [10, 60, "Не можу це зробити!"]
    print("test_process_list passed")

def test_multiplication_table():
    assert multiplication_table(3) == ["3x1=3", "3x2=6", "3x3=9", "3x4=12", "3x5=15", "3x6=18", "3x7=21", "3x8=24"]
    assert multiplication_table(5) == ["5x1=5", "5x2=10", "5x3=15", "5x4=20", "5x5=25"]
    assert multiplication_table(6) == ["6x1=6", "6x2=12", "6x3=18", "6x4=24"]
    print("test_multiplication_table passed")

def test_sum_even_numbers():
    assert sum_even_numbers([1, 2, 3, 4, 5, 6]) == 12
    assert sum_even_numbers([10, 15, 20, 25, 30]) == 60
    assert sum_even_numbers([1, 3, 5, 7]) == 0
    assert sum_even_numbers([2, 4, 6, 8, 10]) == 30
    assert sum_even_numbers([]) == 0
    print("test_sum_even_numbers passed")

if __name__ == '__main__':
    test_calculate_sum_of_numbers()
    test_process_list()
    test_multiplication_table()
    test_sum_even_numbers()
