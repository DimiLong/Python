from enum import Enum
class Directions(Enum):
    LEFT = 'на лево'
    RIGHT = 'на право'
class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police
    def go(self):
        print(f'{self.name} поехала')
    def stop(self):
        print(f'{self.name} остановилась')
    def turn(self, direction):
        print(f'{self.name} повенула {direction.value}')
    def show_speed(self):
        print(f'текущая скорость {self.name} равна {self.speed}')
class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)
    def show_speed(self):
        super().show_speed()
        if self.speed > 60:
            print('Скорость превышена')
class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)
class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)
    def show_speed(self):
        super().show_speed()
        if self.speed > 40:
            print('Скорость превышена')
class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)
car1 = TownCar(120, 'красная', 'TownCar', False)
car2 = SportCar(120, 'красная', 'SportCar', False)
car3 = WorkCar(120, 'красная', 'WorkCar', False)
car4 = PoliceCar(120, 'красная', 'PoliceCar', False)
car1.go()
car1.turn(Directions.LEFT)
car1.turn(Directions.RIGHT)
car1.stop()
car1.show_speed()
car2.show_speed()
car3.show_speed()
car4.show_speed()
car1.speed = 60
car3.speed = 40
car1.show_speed()
car2.show_speed()
car3.show_speed()
car4.show_speed()