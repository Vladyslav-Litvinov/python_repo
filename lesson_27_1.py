from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import unittest

class NovaPoshtaTracker:
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://tracking.novaposhta.ua/#/uk"

    def open(self):
        self.driver.get(self.url)

    def track_parcel(self, track_number):
        input_field = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "input[type='text']"))
        )
        input_field.send_keys(track_number)
        input_field.send_keys(Keys.RETURN)

    def get_status(self):
        status_element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".header__status-text"))
        )
        return status_element.text.strip()  # Видаляємо зайві пробіли

class TestNovaPoshtaTracking(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()  # або інший драйвер
        self.tracker = NovaPoshtaTracker(self.driver)

    def test_tracking_status(self):
        self.tracker.open()
        self.tracker.track_parcel("20451101370338")
        status = self.tracker.get_status()
        print(f"Отриманий статус: {status}")  # Логування
        self.assertEqual(status, "Отримана")  # Оновлено очікуваний статус

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()