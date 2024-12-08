import random

class Animal:
    live = True
    sound = None
    _DEGREE_OF_DANGER = 0

    def __init__(self, speed):
        self._cords = [0, 0, 0]  # Изначальные координаты (X, Y, Z)
        self.speed = speed

    def move(self, dx, dy, dz):
        # Проверяем координаты, если Z становится меньше 0
        if self._cords[2] + dz * self.speed < 0:
            print("It's too deep, i can't dive :(")
        else:
            self._cords[0] += dx * self.speed
            self._cords[1] += dy * self.speed
            self._cords[2] += dz * self.speed

    def get_cords(self):
        x, y, z = self._cords
        print(f"X: {x} Y: {y} Z: {z}")

    def attack(self):
        if self._DEGREE_OF_DANGER < 5:
            print("Sorry, i'm peaceful :)")
        else:
            print("Be careful, i'm attacking you 0_0")

    def speak(self):
        print(self.sound)


class Bird(Animal):
    beak = True  # Утконос имеет клюв

    def lay_eggs(self):
        eggs_count = random.randint(1, 4)  # Случайное количество яиц
        print(f"Here are(is) {eggs_count} eggs for you")


class AquaticAnimal(Animal):
    _DEGREE_OF_DANGER = 3  # Степень опасности

    def dive_in(self, dz):
        dz = abs(dz)  # Берем модуль от dz
        if self._cords[2] - dz < 0:
            print("It's too deep, i can't dive :(")
        else:
            self._cords[2] -= dz  # Уменьшаем координату Z
            self.speed /= 2  # Уменьшаем скорость в два раза


class PoisonousAnimal(Animal):
    _DEGREE_OF_DANGER = 8  # Высокая степень опасности


class Duckbill(PoisonousAnimal, AquaticAnimal, Bird):
    sound = "Click-click-click"  # Издаем звук "Click-click-click"

    def __init__(self, speed):
        super().__init__(speed)  # Инициализируем базовый класс с заданной скоростью


# Пример использования
db = Duckbill(10)

# Вывод информации об утконосе
print(db.live)  # True
print(db.beak)  # True

db.speak()  # Click-click-click
db.attack()  # Be careful, i'm attacking you 0_0

# Перемещение утконоса
db.move(1, 2, 3)  # Перемещаем на 1, 2, 3
db.get_cords()  # Ожидается: X: 10 Y: 20 Z: 30

# Ныряем
db.dive_in(30)  # Ныряем на 30
db.get_cords()  # Ожидается: X: 10 Y: 20 Z: 0

# Утконос откладывает яйца
db.lay_eggs()  # Здесь выводится случайное количество яиц