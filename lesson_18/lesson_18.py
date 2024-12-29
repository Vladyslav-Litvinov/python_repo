# Завдання 1
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

class Manager(Employee):
    def __init__(self, name, salary, department):
        super().__init__(name, salary)
        self.department = department

class Developer(Employee):
    def __init__(self, name, salary, programming_language):
        super().__init__(name, salary)
        self.programming_language = programming_language

class TeamLead(Manager, Developer):
    def __init__(self, name, salary, department, programming_language, team_size):
        # Явный вызов конструктора Employee
        Employee.__init__(self, name, salary)
        # Инициализация атрибутов Manager и Developer
        self.department = department
        self.programming_language = programming_language
        self.team_size = team_size

# Тест для проверки наличия атрибутов
def test_team_lead_attributes():
    tl = TeamLead("Alice", 100000, "IT", "Python", 10)
    assert hasattr(tl, 'name'), "Атрибут 'name' отсутствует"
    assert hasattr(tl, 'salary'), "Атрибут 'salary' отсутствует"
    assert hasattr(tl, 'department'), "Атрибут 'department' отсутствует"
    assert hasattr(tl, 'programming_language'), "Атрибут 'programming_language' отсутствует"
    assert hasattr(tl, 'team_size'), "Атрибут 'team_size' отсутствует"
    print("Все атрибуты присутствуют")

# Выполняем тест
test_team_lead_attributes()

# Завдання 2
from abc import ABC, abstractmethod

class Figure(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

class Square(Figure):
    def __init__(self, side_length):
        self.__side_length = side_length

    def area(self):
        return self.__side_length ** 2

    def perimeter(self):
        return 4 * self.__side_length

class Circle(Figure):
    def __init__(self, radius):
        self.__radius = radius

    def area(self):
        return 3.14159 * self.__radius ** 2

    def perimeter(self):
        return 2 * 3.14159 * self.__radius

class Rectangle(Figure):
    def __init__(self, length, width):
        self.__length = length
        self.__width = width

    def area(self):
        return self.__length * self.__width

    def perimeter(self):
        return 2 * (self.__length + self.__width)

# Створюємо об'єкти фігур
figures = [
    Square(4),
    Circle(3),
    Rectangle(5, 3)
]
# Розраховуємо та виводимо площу та периметр кожної фігури
for figure in figures:
    print(f"Фігура: {figure.__class__.__name__}")
    print(f"Площа: {figure.area()}")
    print(f"Периметр: {figure.perimeter()}")
    print("-" * 20)
