"""еализовать базовый класс Worker (работник), в котором определить атрибуты:
name, surname, position (должность), income (доход). Последний атрибут должен
быть защищенным и ссылаться на словарь, содержащий элементы: оклад и премия,
например, {"wage": wage, "bonus": bonus}. Создать класс Position (должность)
на базе класса Worker. В классе Position реализовать методы получения полного
имени сотрудника (get_full_name) и дохода с учетом премии (get_total_income).
Проверить работу примера на реальных данных (создать экземпляры класса Position
,передать данные, проверить значения атрибутов, вызвать методы экземпляров)."""


class Worker:
    name = None
    surname = None
    position = None
    wage = None
    bonus = None
    _income = {"оклад": wage, "пермия": bonus}

    def __init__(self, name, surname, position, income):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = income


class Position(Worker):
    def __init__(self, name, surname, position, income):
        super().__init__(name, surname, position, income)

    def get_full_name(self):
        return f"{self.name} {self.surname} {self.position}"

    def get_total_income(self, wage, bonus):
        self.wage = wage
        self.bonus = bonus
        self._income = {"Оклад": wage, "Премия": bonus}
        return self._income


team_lead = Position("Галкин", "Дмитрий", "Тимлид", "")
print(f"{team_lead.get_full_name()} {team_lead.get_total_income(100, 500)}")
