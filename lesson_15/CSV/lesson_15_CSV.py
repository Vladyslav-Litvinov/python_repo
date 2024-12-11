# Завдання 1:
# Візміть два файли з теки ideas_for_test/work_with_csv порівняйте на наявність дублікатів і приберіть їх.
# Результат запишіть у файл result_<your_second_name>.csv

import csv
import os


def read_csv_to_set(filename):
    with open(filename, newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        data_set = set(tuple(row) for row in reader)
    return data_set


def write_set_to_csv(data_set, filename):
    with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        for row in data_set:
            writer.writerow(row)


def remove_duplicates(file1, file2, output_file):
    if not os.path.exists(file1):
        print(f"Файл {file1} не знайдено.")
        return
    if not os.path.exists(file2):
        print(f"Файл {file2} не знайдено.")
        return

    data1 = read_csv_to_set(file1)
    data2 = read_csv_to_set(file2)
    combined_data = data1 | data2
    write_set_to_csv(combined_data, output_file)
    print(f"Файл {output_file} успішно створено.")

file1 = "random.csv"
file2 = "random-michaels.csv"
output_file = "our_result_without_duplicate.csv"
remove_duplicates(file1, file2, output_file)


