from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
import time

# Ініціалізація веб-драйвера
driver = webdriver.Chrome()

try:
    print("Відкриття сторінки з фреймами...")
    driver.get("http://localhost:8000/dz.html")

    # Переключення на перший фрейм
    print("Переключення на перший фрейм...")
    driver.switch_to.frame("frame1")

    # Введення секретного тексту в першому фреймі
    print("Введення секретного тексту в першому фреймі...")
    input1 = driver.find_element(By.ID, "input1")
    input1.send_keys("Frame1_Secret")

    # Натискання кнопки "Перевірити" в першому фреймі
    print("Натискання кнопки 'Перевірити' в першому фреймі...")
    button1 = driver.find_element(By.XPATH, "//button[text()='Перевірити']")
    button1.click()

    # Очікування появи діалогового вікна та перевірка тексту
    print("Очікування діалогового вікна...")
    time.sleep(1)  # Чекаємо, поки з'явиться діалогове вікно
    alert = Alert(driver)
    alert_text = alert.text
    print(f"Текст діалогового вікна: {alert_text}")
    assert alert_text == "Верифікація пройшла успішно!"
    alert.accept()

    # Повернення до основного контенту сторінки
    print("Повернення до основного контенту сторінки...")
    driver.switch_to.default_content()

    # Переключення на другий фрейм
    print("Переключення на другий фрейм...")
    driver.switch_to.frame("frame2")

    # Введення секретного тексту в другому фреймі
    print("Введення секретного тексту в другому фреймі...")
    input2 = driver.find_element(By.ID, "input2")
    input2.send_keys("Frame2_Secret")

    # Натискання кнопки "Перевірити" в другому фреймі
    print("Натискання кнопки 'Перевірити' в другому фреймі...")
    button2 = driver.find_element(By.XPATH, "//button[text()='Перевірити']")
    button2.click()

    # Очікування появи діалогового вікна та перевірка тексту
    print("Очікування діалогового вікна...")
    time.sleep(1)  # Чекаємо, поки з'явиться діалогове вікно
    alert = Alert(driver)
    alert_text = alert.text
    print(f"Текст діалогового вікна: {alert_text}")
    assert alert_text == "Верифікація пройшла успішно!"
    alert.accept()

    print("Тести пройшли успішно!")

finally:
    # Закриття браузера
    print("Закриття браузера...")
    driver.quit()