# Порахувати кількість унікальних символів в строці. Якщо їх більше 10 - вивести в консоль True, інакше - False. Строку отримати за допомогою функції input()
input_string = input("Enter a string: ")
unique_characters = set(input_string)
result = len(unique_characters) > 10
print(result)