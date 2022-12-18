"""5) Реализовать класс Stationery (канцелярская принадлежность). Определить в
нем атрибут title (название) и метод draw (отрисовка). Метод выводит сообщение
“Запуск отрисовки.” Создать три дочерних класса Pen (ручка), Pencil (карандаш),
 Handle (маркер). В каждом из классов реализовать переопределение метода draw.
  Для каждого из классов метод должен выводить уникальное сообщение. Создать
  экземпляры классов и проверить, что выведет описанный метод для каждого
  экземпляра."""


class Stationery:
    title = "Название"

    def draw(self):
        print(f"Запуск отрисовки")


class Pen(Stationery):
    def draw(self):
        print(f"Отрисовка ручкой")


class Pencil(Stationery):
    def draw(self):
        print(f"Отрисовка карандашом")


class Handle(Stationery):
    def draw(self):
        print(f"Отрисовка маркером")


user_pen = Pen()
user_pen.draw()

user_pencil = Pencil()
user_pencil.draw()

user_handle = Handle()
user_handle.draw()
