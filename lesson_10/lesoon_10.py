# Є ліст з числами, порахуйте сумму усіх ПАРНИХ чисел в цьому лісті
numbers = list(range(1, 21))
even_numbers = [num for num in numbers if num % 2 == 0]
sum_even = sum(even_numbers)

print("Even numbers:", even_numbers)
print("Sum of even numbers:", sum_even)