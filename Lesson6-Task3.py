class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = { 'wage': wage, 'bonus': bonus }
class Position(Worker):
    def __init__(self, name, surname, position, wage, bonus):
        super().__init__(name, surname, position, wage, bonus)
    def get_full_name(self):
        return f'{self.name} {self.surname}'
    def get_total_income(self):
        return self._income['wage'] + self._income['bonus']
position1 = Position('Dmitry', 'Strebkov', 'Pre-sale engineer', 5, 0.7)
print(position1.get_full_name())
print(position1.get_total_income())
print(position1.name)
print(position1.surname)
print(position1.position)
print(position1._income)