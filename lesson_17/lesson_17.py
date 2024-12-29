class Rhombus:
    def __init__(self, side_a, angle_a):
        self.side_a = side_a
        self.angle_a = angle_a

    def __setattr__(self, name, value):
        if name == "side_a":
            if value <= 0:
                raise ValueError("Значение стороны должно быть больше 0.")
        if name in ["angle_a", "angle_b"]:
            if not (0 < value < 180):
                raise ValueError("Угол должен быть между 0 и 180 градусами.")
            # Проверяем сумму углов при установке одного из углов
            other_angle = 180 - value if name == "angle_a" else 180 - value
            if name == "angle_a" and hasattr(self, "angle_b") and other_angle != self.angle_b:
                raise ValueError("Сумма углов должна быть равна 180 градусам.")
            if name == "angle_b" and hasattr(self, "angle_a") and other_angle != self.angle_a:
                raise ValueError("Сумма углов должна быть равна 180 градусам.")
            super().__setattr__("angle_b" if name == "angle_a" else "angle_a", other_angle)

        super().__setattr__(name, value)

    def __str__(self):
        return f"Ромб со стороной {self.side_a} и углами {self.angle_a}° и {self.angle_b}°."


# Пример использования класса:
try:
    rhombus = Rhombus(4, 80)
    print(rhombus)
    rhombus.angle_b = 100  # Это вызовет ошибку
except ValueError as e:
    print(e)