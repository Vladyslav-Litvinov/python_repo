class Rhombus:
    def __init__(self, side_a, angle_a):
        self.side_a = side_a
        self.angle_a = angle_a

    def __setattr__(self, name, value):
        if name == "side_a" and value <= 0:
            raise ValueError("Значення сторони повинно бути більше 0")
        if name == "angle_a":
            if not (0 < value < 180):
                raise ValueError("Кут повинен бути між 0 і 180 градусами")
            self.__dict__[name] = value
            self.__dict__["angle_b"] = 180 - value
        else:
            self.__dict__[name] = value

    def __str__(self):
        return f"Ромб зі стороною {self.side_a} і кутами {self.angle_a}° та {self.angle_b}°"

# Приклад використання
try:
    rhombus = Rhombus(4, 66)
    print(rhombus)
except ValueError as e:
    print(e)