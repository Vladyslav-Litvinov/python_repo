#alice_in_wonderland = '"Would you tell me, please, which way I ought to go from here?"\n"That depends a good deal on where you want to get to," said the Cat.\n"I don't much care where ——" said Alice.\n"Then it doesn't matter which way you go," said the Cat.\n"—— so long as I get somewhere," Alice added as an explanation.\n"Oh, you're sure to do that," said the Cat, "if you only walk long enough."'
# task 01 == Розділіть змінну alice_in_wonderland так, щоб вона займала декілька фізичних лінії
# task 02 == Знайдіть та відобразіть всі символи одинарної лапки (') у тексті
# task 03 == Виведіть змінну alice_in_wonderland на друк


"""
    # Задачі 04 -10:
    # Переведіть задачі з книги "Математика, 5 клас"
    # на мову пітон і виведіть відповідь, так, щоб було
    # зрозуміло дитині, що навчається в п'ятому класі
"""
# task 04
"""
Площа Чорного моря становить 436 402 км2, а площа Азовського
моря становить 37 800 км2. Яку площу займають Чорне та Азов-
ське моря разом?
"""


# task 05
"""
Мережа супермаркетів має 3 склади, де всього розміщено
375 291 товар. На першому та другому складах перебуває
250 449 товарів. На другому та третьому – 222 950 товарів.
Знайдіть кількість товарів, що розміщені на кожному складі.
"""


# task 06
"""
Михайло разом з батьками вирішили купити комп’ютер, ско-
риставшись послугою «Оплата частинами». Відомо, що сплачу-
вати необхідно буде півтора року по 1179 грн/місяць. Обчисліть
вартість комп’ютера.
"""


# task 07
"""
Знайди остачу від діленя чисел:
a) 8019 : 8     d) 7248 : 6
b) 9907 : 9     e) 7128 : 5
c) 2789 : 5     f) 19224 : 9
"""


# task 08
"""
Іринка, готуючись до свого дня народження, склала список того,
що їй потрібно замовити. Обчисліть, скільки грошей знадобиться
для даного її замовлення.
Назва товару    Кількість   Ціна
Піца велика     4           274 грн
Піца середня    2           218 грн
Сік             4           35 грн
Торт            1           350 грн
Вода            3           21 грн
"""


# task 09
"""
Ігор займається фотографією. Він вирішив зібрати всі свої 232
фотографії та вклеїти в альбом. На одній сторінці може бути
розміщено щонайбільше 8 фото. Скільки сторінок знадобиться
Ігорю, щоб вклеїти всі фото?
"""


# task 10
"""
Родина зібралася в автомобільну подорож із Харкова в Буда-
пешт. Відстань між цими містами становить 1600 км. Відомо,
що на кожні 100 км необхідно 9 літрів бензину. Місткість баку
становить 48 літрів.
1) Скільки літрів бензину знадобиться для такої подорожі?
2) Скільки щонайменше разів родині необхідно заїхати на зап-
равку під час цієї подорожі, кожного разу заправляючи пов-
ний бак?
"""
# task 01
alice_in_wonderland = (
    "Would you tell me, please, which way I ought to go from here?\n"
    "That depends a good deal on where you want to get to, said the Cat.\n"
    "I don't much care where —— said Alice.\n"
    "Then it doesn't matter which way you go, said the Cat.\n"
    "—— so long as I get somewhere, Alice added as an explanation.\n"
    "Oh, you're sure to do that, said the Cat, if you only walk long enough."
)

# task 02
single_quote_count = alice_in_wonderland.count("'")
print("Кількість одинарних лапок у тексті:", single_quote_count)

# task 03
print(alice_in_wonderland)

# task 04
area_black_sea = 434402
area_azov_sea = 37800
total_area = area_black_sea + area_azov_sea
print("Сумарна площа Чорного та Азовського морів:", total_area, "км2")

# task 05
total_products = 375291
products_first_second = 250449
products_second_third = 222950

number_first_storage = 375291 - 222950  # Кількість товарів на першому складі
number_second_storage = 250449 - number_first_storage  # Кількість товарів на другому складі
number_third_storage = total_products - number_first_storage - number_second_storage  # Кількість товарів на третьому складі

print("Кількість товарів на першому складі:", number_first_storage)
print("Кількість товарів на другому складі:", number_second_storage)
print("Кількість товарів на третьому складі:", number_third_storage)

# task 06
monthly_payment = 1179  # грн
months = 1.5 * 12        # 1.5 роки
total_cost = monthly_payment * months
print("Вартість комп'ютера:", total_cost, "грн")

# task 07
number_one_a = 8019
number_two_a = 8
result_a = number_one_a % number_two_a
print("Остача від ділення", number_one_a, "на", number_two_a, "a:", result_a)

number_one_b = 9907
number_two_b = 9
result_b = number_one_b % number_two_b
print("Остача від ділення", number_one_b, "на", number_two_b, "b:", result_b)

number_one_c = 2789
number_two_c = 5
result_c = number_one_c % number_two_c
print("Остача від ділення", number_one_c, "на", number_two_c, "c:", result_c)

number_one_d = 7248
number_two_d = 6
result_d = number_one_d % number_two_d
print("Остача від ділення", number_one_d, "на", number_two_d, "d:", result_d)

number_one_e = 7128
number_two_e = 5
result_e = number_one_e % number_two_e
print("Остача від ділення", number_one_e, "на", number_two_e, "e:", result_e)

number_one_f = 19224
number_two_f = 9
result_f = number_one_f % number_two_f
print("Остача від ділення", number_one_f, "на", number_two_f, "f:", result_f)

# task 08
pizza_large_price = 274
pizza_medium_price = 218
juice_price = 35
cake_price = 350
water_price = 21

quantity_large_pizza = 4
quantity_medium_pizza = 2
quantity_juice = 4
quantity_cake = 1
quantity_water = 3

total_cost_order = (pizza_large_price * quantity_large_pizza +
                    pizza_medium_price * quantity_medium_pizza +
                    juice_price * quantity_juice +
                    cake_price * quantity_cake +
                    water_price * quantity_water)

print("Загальна вартість замовлення:", total_cost_order, "грн")

# task 09
total_photos = 232
photos_per_page = 8
total_pages = total_photos // photos_per_page + 1

print("Кількість сторінок, необхідних для фотографій:", total_pages)

# task 10
distance = 1600
fuel_per_100km = 9
tank_capacity = 48

total_fuel_needed = (distance / 100) * fuel_per_100km
refuels_needed = total_fuel_needed / tank_capacity + 1

print("Кількість літрів бензину, що знадобиться:", total_fuel_needed)
print("Кількість заправок під час подорожі:", refuels_needed)
