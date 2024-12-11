# Завдання 2:
# Провалідуйте, чи усі файли у папці ideas_for_test/work_with_json є валідними json.
# Результат для невалідного файлу виведіть через логер на рівні еррор у файл json__<your_second_name>.log

import os
import json
import logging
from pathlib import Path

def validate_json_files(directory, log_file):
    logging.basicConfig(filename=log_file, level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
    logger = logging.getLogger("json_validator")

    for root, _, files in os.walk(directory):
        for filename in files:
            if filename.endswith(".json"):
                filepath = os.path.join(root, filename)
                print(f"Перевіряється файл: {filepath}")
                logger.info(f"Перевіряється файл: {filepath}")
                try:
                    with open(filepath, 'r', encoding='utf-8') as file:
                        content = file.read()
                        logger.debug(f"Вміст файлу {filename}: {content}")

                        try:
                            json.loads(content)
                            print(f"Файл {filepath} є валідним JSON")
                        except json.JSONDecodeError as e:
                            logger.error(f"Файл {filepath} не є валідним JSON: {e}")
                            print(f"Помилка: Файл {filepath} не є валідним JSON: {e}")
                except UnicodeDecodeError as e:
                    logger.error(f"Файл {filepath} містить некоректні символи: {e}")
                    print(f"Помилка: Файл {filepath} містить некоректні символи: {e}")

current_directory = Path(__file__).parent
json_directory = current_directory
log_file = json_directory / "json_our_invalid_file.log"
validate_json_files(json_directory, log_file)
print("Перевірка завершена")

















