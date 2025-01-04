# Генератор, який повертає послідовність парних чисел від 0 до N
def even_numbers(N):
    for i in range(0, N+1, 2):
        yield i
for num in even_numbers(10):
    print(num)

# Генератор, який генерує послідовність Фібоначчі до певного числа N
def fibonacci(N):
    a, b = 0, 1
    while a <= N:
        yield a
        a, b = b, a + b
for num in fibonacci(10):
    print(num)

# Ітератор для зворотного виведення елементів списку
class ReverseIterator:
    def __init__(self, lst):
        self.lst = lst
        self.index = len(lst)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index -= 1
        return self.lst[self.index]
lst = [1, 2, 3, 4, 5]
for item in ReverseIterator(lst):
    print(item)

# Ітератор, який повертає всі парні числа в діапазоні від 0 до N
class EvenIterator:
    def __init__(self, N):
        self.N = N
        self.current = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current > self.N:
            raise StopIteration
        result = self.current
        self.current += 2
        return result
for num in EvenIterator(10):
    print(num)

# Декоратор, який логує аргументи та результати викликаної функції
def log_function_call(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print(f"Function {func.__name__} called with arguments {args} and {kwargs}. Result: {result}")
        return result
    return wrapper
@log_function_call
def add(a, b):
    return a + b

add(3, 4)

# Декоратор, який перехоплює та обробляє винятки, які виникають в ході виконання функції
def exception_handler(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            print(f"Exception occurred in function {func.__name__}: {e}")
    return wrapper

# Приклад використання
@exception_handler
def divide(a, b):
    return a / b

divide(10, 0)
