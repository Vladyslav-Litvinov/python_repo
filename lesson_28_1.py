import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from faker import Faker

fake = Faker()

# Фікстура для ініціалізації драйвера
@pytest.fixture(scope="module")
def driver():
    # Ручне вказання шляху до Chrome
    chrome_path = r"C:\Users\Vlad\Desktop\chrome-win64\chrome.exe"
    service = Service()
    options = webdriver.ChromeOptions()
    options.binary_location = chrome_path
    driver = webdriver.Chrome(service=service, options=options)
    yield driver
    driver.quit()

# Клас для пошуку елементів (PageObject)
class MainPage:
    def __init__(self, driver):
        self.driver = driver
        self.sign_in_button = (By.XPATH, "//button[contains(@class, 'header_signin')]") # Локатор для кнопки "Sign In"

    def find_element(self, locator):
        return WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(locator)) # Очікування появи елемента

# Клас для пошуку елементів (PageObject)
class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.registration_button = (By.XPATH, "//button[contains(@class, 'btn-link') and text()='Registration']") # Локатор для кнопки "Registration"

    def find_element(self, locator):
        return WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(locator)) # Очікування появи елемента

# Клас для пошуку елементів (PageObject)
class RegistrationPage:
    def __init__(self, driver):
        self.driver = driver
        self.name_field = (By.ID, "signupName") # Локатор для поля "Name"
        self.last_name_field = (By.ID, "signupLastName") # Локатор для поля "Last Name"
        self.email_field = (By.ID, "signupEmail") # Локатор для поля "Email"
        self.password_field = (By.ID, "signupPassword") # Локатор для поля "Password"
        self.re_enter_password_field = (By.ID, "signupRepeatPassword") # Локатор для поля "Re-enter password"
        self.register_button = (By.XPATH, "//button[text()='Register']") # Локатор для кнопки "Register"
        self.registration_complete_message = (By.XPATH, "//p[text()='Registration complete']") # Локатор для повідомлення про успішну реєстрацію

    def find_element(self, locator):
        return WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(locator)) # Очікування появи елемента

# Фікстура для ініціалізації головної сторінки з логіном
@pytest.fixture(scope="module")
def main_page(driver):
    driver.get("https://guest:welcome2qauto@qauto2.forstudy.space/") # Відкриття головної сторінки
    return MainPage(driver)

# Фікстура для ініціалізації сторінки входу
@pytest.fixture(scope="module")
def login_page(driver):
    return LoginPage(driver)

# Фікстура для ініціалізації сторінки реєстрації
@pytest.fixture(scope="module")
def registration_page(driver):
    return RegistrationPage(driver)

# Тест для створення користувача
def test_create_user(driver, main_page, login_page, registration_page):
    # Натискання кнопки "Sign In" на головній сторінці
    sign_in_button = main_page.find_element(main_page.sign_in_button)
    sign_in_button.click()

    # Дочекатися завантаження сторінки входу
    WebDriverWait(driver, 10).until(EC.presence_of_element_located(login_page.registration_button))

    # Натискання кнопки "Registration" на сторінці входу
    registration_button = login_page.find_element(login_page.registration_button)
    registration_button.click()

    # Дочекатися завантаження сторінки реєстрації
    WebDriverWait(driver, 10).until(EC.presence_of_element_located(registration_page.name_field))

    # Знайти елементи полів реєстрації
    name_field = registration_page.find_element(registration_page.name_field)
    last_name_field = registration_page.find_element(registration_page.last_name_field)
    email_field = registration_page.find_element(registration_page.email_field)
    password_field = registration_page.find_element(registration_page.password_field)
    re_enter_password_field = registration_page.find_element(registration_page.re_enter_password_field)

    # Генерація випадкових даних
    random_name = fake.first_name()
    random_last_name = fake.last_name()
    random_email = fake.email()
    random_password = fake.password(length=10, special_chars=False, digits=True, upper_case=True, lower_case=True)

    # Заповнення полів реєстрації
    name_field.send_keys(random_name)
    last_name_field.send_keys(random_last_name)
    email_field.send_keys(random_email)
    password_field.send_keys(random_password)
    re_enter_password_field.send_keys(random_password)

    # Натискання кнопки "Register"
    register_button = registration_page.find_element(registration_page.register_button)
    register_button.click()

    # Перевірка появи повідомлення про успішну реєстрацію
    WebDriverWait(driver, 10).until(EC.presence_of_element_located(registration_page.registration_complete_message))
    assert "Registration complete" in driver.page_source, "Реєстрація не виконана!"

# Запуск тесту
if __name__ == "__main__":
    pytest.main(["-v", "test_registration.py"])