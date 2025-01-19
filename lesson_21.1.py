import requests

BASE_URL = "http://127.0.0.1:8080"
IMAGE_PATH = "example.jpg"

# 1. Завантаження зображення
print("Завантаження зображення...")
with open(IMAGE_PATH, "rb") as img_file:
    upload_response = requests.post(f"{BASE_URL}/upload", files={"image": img_file})

if upload_response.status_code == 201:
    print("Зображення завантажено успішно!")
    upload_data = upload_response.json()
    print("URL зображення:", upload_data.get("image_url"))
else:
    print("Помилка завантаження:", upload_response.json())
    exit()

# 2. Отримання URL зображення
filename = upload_data.get("image_url").split("/")[-1]
print("\nОтримання URL зображення...")
get_response = requests.get(f"{BASE_URL}/image/{filename}", headers={"Content-Type": "text"})

if get_response.status_code == 200:
    print("Отримано URL зображення:", get_response.json().get("image_url"))
else:
    print("Помилка отримання зображення:", get_response.json())

# 3. Видалення зображення
print("\nВидалення зображення...")
delete_response = requests.delete(f"{BASE_URL}/delete/{filename}")

if delete_response.status_code == 200:
    print("Зображення видалено:", delete_response.json().get("message"))
else:
    print("Помилка видалення:", delete_response.json())
