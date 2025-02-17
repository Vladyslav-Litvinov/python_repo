from flask import Flask, request, jsonify
from flask_jwt_extended import JWTManager, jwt_required, create_access_token

app = Flask(__name__)

app.config['JWT_SECRET_KEY'] = 'super-secret'  # Змініть на свій секретний ключ
jwt = JWTManager(app)

cars_db = {
    1: {"brand": "BMW", "year": 2018, "engine_volume": 2.0, "price": 50000},
    2: {"brand": "Audi", "year": 2020, "engine_volume": 1.8, "price": 45000},
    3: {"brand": "Mercedes", "year": 2019, "engine_volume": 2.5, "price": 55000},
    4: {"brand": "Toyota", "year": 2017, "engine_volume": 2.4, "price": 35000},
    5: {"brand": "Honda", "year": 2016, "engine_volume": 1.6, "price": 30000},
    6: {"brand": "Nissan", "year": 2021, "engine_volume": 1.5, "price": 40000},
    7: {"brand": "Ford", "year": 2015, "engine_volume": 2.2, "price": 32000},
    8: {"brand": "Chevrolet", "year": 2018, "engine_volume": 1.8, "price": 28000},
    9: {"brand": "Volkswagen", "year": 2019, "engine_volume": 2.0, "price": 33000},
    10: {"brand": "Hyundai", "year": 2020, "engine_volume": 1.6, "price": 29000},
    11: {"brand": "Kia", "year": 2019, "engine_volume": 2.0, "price": 31000},
    12: {"brand": "Subaru", "year": 2017, "engine_volume": 2.5, "price": 40000},
    13: {"brand": "Mazda", "year": 2018, "engine_volume": 2.0, "price": 32000},
    14: {"brand": "Lexus", "year": 2021, "engine_volume": 3.0, "price": 60000},
    15: {"brand": "Infiniti", "year": 2019, "engine_volume": 3.5, "price": 52000},
    16: {"brand": "Acura", "year": 2020, "engine_volume": 2.4, "price": 48000},
    17: {"brand": "Jeep", "year": 2018, "engine_volume": 3.6, "price": 45000},
    18: {"brand": "Land Rover", "year": 2020, "engine_volume": 2.0, "price": 55000},
    19: {"brand": "Volvo", "year": 2019, "engine_volume": 2.0, "price": 46000},
    20: {"brand": "Porsche", "year": 2021, "engine_volume": 3.0, "price": 70000},
    21: {"brand": "Tesla", "year": 2020, "engine_volume": 0.0, "price": 80000},
    22: {"brand": "Ferrari", "year": 2021, "engine_volume": 6.3, "price": 250000},
    23: {"brand": "Lamborghini", "year": 2020, "engine_volume": 6.5, "price": 300000},
    24: {"brand": "Bugatti", "year": 2019, "engine_volume": 8.0, "price": 350000},
    25: {"brand": "McLaren", "year": 2021, "engine_volume": 4.0, "price": 280000},
}

users = {
    "test_user": "test_pass"
}

def authenticate(username, password):
    if username in users and users[username] ==  password:
        return username

def identity(payload):
    username = payload['identity']
    return {"username": username}

@app.route('/auth', methods=['POST'])
def login():
    auth = request.authorization
    if not auth or not auth.username or not auth.password:
        return jsonify({"message": "Аутентифікація не пройшла!"}), 401

    username = authenticate(auth.username, auth.password)
    if not username:
        return jsonify({"message": "Неправильне ім'я користувача або пароль!"}), 401

    access_token = create_access_token(identity=username)
    return jsonify(access_token=access_token), 200

@app.route('/cars', methods=['GET'])
@jwt_required()
def get_cars():
    sort_by = request.args.get('sort_by')
    limit = request.args.get('limit')

    # Перевірка на числове значення для limit
    if limit:
        try:
            limit = int(limit)
        except ValueError:
            return jsonify({"message": "Limit must be a number!"}), 400
    else:
        limit = len(cars_db)

    if sort_by:
        sorted_cars = sorted(cars_db.values(), key=lambda x: x.get(sort_by, 0))
    else:
        sorted_cars = sorted(cars_db.values(), key=lambda x: x['brand'])

    limited_cars = sorted_cars[:limit]

    return jsonify(limited_cars), 200

if __name__ == '__main__':
    host = '127.0.0.1'
    port = 8080
    app.run(host=host, port=port, debug=True)
