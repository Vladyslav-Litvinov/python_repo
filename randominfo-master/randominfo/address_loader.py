import csv
import os
import random

def load_addresses():
    allAddrs = []
    filepath = os.path.join(os.path.dirname(__file__), 'data.csv')
    with open(filepath, newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            if any(row):  # Проверка на непустую строку
                allAddrs.append(", ".join(row[-4:]))  # Соединяем последние 4 элемента строки
    return allAddrs

allAddrs = load_addresses()

def get_address():
    if not allAddrs:
        raise ValueError("Список адресов пуст. Проверьте данные в 'data.csv'.")
    full_addr = random.choice(allAddrs)
    return full_addr

# Пример использования
if __name__ == "__main__":
    print(get_address())
