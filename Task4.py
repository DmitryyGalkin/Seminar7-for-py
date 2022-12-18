"""4) Реализуйте базовый класс Car. У данного класса должны быть следующие
атрибуты: speed, color, name, is_police (булево). А также методы: go, stop,
turn(direction), которые должны сообщать, что машина поехала, остановилась,
повернула (куда). Опишите несколько дочерних классов: TownCar, SportCar,
WorkCar, PoliceCar. Добавьте в базовый класс метод show_speed, который должен
показывать текущую скорость автомобиля. Для классов TownCar и WorkCar
переопределите метод show_speed. При значении скорости свыше 60 (TownCar) и
40 (WorkCar) должно выводиться сообщение о превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к
атрибутам, выведите результат. Выполните вызов методов и также покажите
результат."""


class Car:
    speed = None
    color = None
    name = None
    is_police = False

    def __init__(self, name, speed, color, is_police):
        self.name = name
        self.speed = speed
        self.color = color
        self.is_police = is_police

    def go(self):
       return (f"Машина {self.name} тронулась")

    def stop(self):
        return (f"Машина  {self.name}  остановилась")

    def turn(self, direction):
        return (f"Машина {self.name}  повернула {direction}")

    def show_speed(self, speed):
        return (f"Текущая скорость автомобиля {self.name} : {self.speed} km/h")


class TownCar(Car):
    def __init__(self, name, speed, color, is_police):
        super().__init__(name, speed, color, is_police)

    def show_speed(self, speed):
        self.speed = speed
        if speed > 60:
            print(f"Текущая скорость автомобиля: {self.speed} km/h.Вы превысили "
                  f"скорость!")
        else:
            (f"Текущая скорость автомобиля: {self.speed} km/h")


class SportCar(Car):
    def __init__(self, name, speed, color, is_police):
        super().__init__(name, speed, color, is_police)


class WorkCar(Car):
    def __init__(self, name, speed, color, is_police):
        super().__init__(name, speed, color, is_police)

    def show_speed(self, speed):
        self.speed = speed
        if speed > 60:
            print(f"Текущая скорость автомобиля: {speed} km/h.Вы превысили "
                  f"скорость!")
        else:
            (f"Текущая скорость автомобиля: {speed} km/h")


class PoliceCar(Car):
    def __init__(self, name, speed, color):
        super().__init__(name, speed, color, "True")


volvo = TownCar("Volvo", 60, "red", "False")
lada = WorkCar("Lada", 90, "black", "False")
gaz = PoliceCar("Gaz", 50, "blue")
lamba = SportCar("Lamba", 210, "blanche", "False")

print(volvo.is_police)
print(lada.turn("Направо"))
print(gaz.go(), gaz.is_police)
print(gaz.show_speed(90))
print(lamba.stop())
print(lamba.is_police)
print(volvo.show_speed())