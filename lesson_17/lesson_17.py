class Rhombus:
    def __init__(self, side_a, angle_a):
        self.side_a = side_a
        self.angle_a = angle_a

    def __setattr__(self, name, value):
        if name == "side_a":
            if value <= 0:
                raise ValueError("Значення сторони повинно бути більше 0.")
        if name in ["angle_a", "angle_b"]:
            if not (0 < value < 180):
                raise ValueError("Кут повинен бути між 0 та 180 градусів.")
            # Перевіряємо суму кутів при встановленні одного з кутів
            other_angle = 180 - value if name == "angle_a" else 180 - value
            if name == "angle_a" and hasattr(self, "angle_b") and other_angle != self.angle_b:
                raise ValueError("Сума кутів повинна бути рівна 180 градусів.")
            if name == "angle_b" and hasattr(self, "angle_a") and other_angle != self.angle_a:
                raise ValueError("Сума кутів повинна бути рівна 180 градусів.")
            super().__setattr__("angle_b" if name == "angle_a" else "angle_a", other_angle)

        super().__setattr__(name, value)

    def __str__(self):
        return f"Ромб зі стороною {self.side_a} і кутами {self.angle_a}° та {self.angle_b}°."
# Приклад використання класу:
try:
    rhombus = Rhombus(4, 66)
    print(rhombus)
    rhombus.angle_b = 50  # Це викличе помилку
except ValueError as e:
    print(e)