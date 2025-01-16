import requests

url = 'https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos'
params = {'sol': 1000, 'camera': 'fhaz', 'api_key': 'DEMO_KEY'}
num_photos_to_download = 2  # Количество фотографий для загрузки

try:
    response = requests.get(url, params=params)
    print(f"Статус код ответа API: {response.status_code}")
    response.raise_for_status()

    data = response.json()
    print(f"JSON ответ API:\n{data}")

    if data['photos']:
        for i, photo in enumerate(data['photos'][:num_photos_to_download]): # Ограничение цикла
            photo_url = photo['img_src']
            print(f"URL фотографии {i+1}: {photo_url}")
            filename = f"mars_photo{i+1}.jpg"

            try:
                photo_response = requests.get(photo_url, stream=True)
                photo_response.raise_for_status()

                with open(filename, 'wb') as f:
                    for chunk in photo_response.iter_content(1024):
                        f.write(chunk)

                print(f"Фото {filename} загружено")
            except requests.exceptions.RequestException as e:
                print(f"Ошибка загрузки фото: {e}")

    else:
        print("Фотографий не найдено по заданным параметрам.")

except requests.exceptions.RequestException as e:
    print(f"Ошибка запроса к API: {e}")
except (KeyError, TypeError) as e:
    print(f"Ошибка обработки JSON: {e}")