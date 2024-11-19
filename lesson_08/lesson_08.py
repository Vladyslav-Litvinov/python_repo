# Напишіть цикл, який буде вимагати від користувача ввести слово, в якому є літера "h" (враховуються як великі так і маленькі).
# Цикл не повинен завершитися, якщо користувач ввів слово без букви "h".
while True:
    word = input("Enter a word containing the letter 'h': ")
    if 'h' in word.lower():
        print("Thank you!")
        break
    print("The word does not contain the letter 'h'. Try again.")