import pytest
import requests
import logging
from requests.auth import HTTPBasicAuth

# Налаштування логування для консолі та файлу
logging.basicConfig(level=logging.INFO, filename="test_search.log", filemode="w",
                    format="%(asctime)s - %(levelname)s - %(message)s")
console = logging.StreamHandler()
console.setLevel(logging.INFO)
formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
console.setFormatter(formatter)
logging.getLogger().addHandler(console)

logger = logging.getLogger()

BASE_URL = "http://127.0.0.1:8080"
USERNAME = "test_user"
PASSWORD = "test_pass"


@pytest.fixture(scope='class')
def auth_session():
    session = requests.Session()
    auth_response = session.post(f"{BASE_URL}/auth", auth=HTTPBasicAuth(USERNAME, PASSWORD))
    assert auth_response.status_code == 200, "Authentication failed"
    access_token = auth_response.json().get("access_token")
    assert access_token, "No access token received"
    session.headers.update({"Authorization": f"Bearer {access_token}"})
    return session


@pytest.mark.parametrize("sort_by,limit", [
    ("price", "5"),
    ("year", "3"),
    ("engine_volume", "7"),
    ("brand", "10"),
    (None, "4"),
    ("price", None),
    (None, None)
])
def test_get_cars(auth_session, sort_by, limit):
    logger.info(f"Test with sort_by={sort_by}, limit={limit} started.")  # Логування початку тесту
    params = {}
    if sort_by:
        params["sort_by"] = sort_by
    if limit:
        params["limit"] = limit

    response = auth_session.get(f"{BASE_URL}/cars", params=params)
    assert response.status_code == 200, "Failed to fetch cars"
    cars = response.json()
    assert isinstance(cars, list), "Response is not a list"

    # Додаткові перевірки
    if limit:
        assert len(cars) <= int(limit), "Returned more cars than requested"
    if sort_by:
        sorted_cars = sorted(cars, key=lambda x: x.get(sort_by, 0))
        assert cars == sorted_cars, "Cars are not sorted correctly"

    logger.info(f"Test with sort_by={sort_by}, limit={limit} passed successfully.")  # Логування успіху тесту
