from enum import Enum
from time import sleep
class Color(Enum):
    RED = 'Красный'
    YELLOW = 'Желтый'
    GREEN = 'Зеленый'
class TrafficLight:
    def __init__(self):
        self.__color = Color.RED
    @property
    def color(self):
        return self.__color
    @color.setter
    def color(self, value):
        if isinstance(value, Color):
            self.__color = value
        else:
            raise TypeError('Некорректный тип устанавливаемого значения. ожидаемый тип Color')
    def running(self, numOfCycles):
        waitedState = Color.RED
        currentCycle = 0
        sleepTimeout = 0
        while currentCycle < numOfCycles:
            if waitedState == Color.RED and (self.color == Color.GREEN or currentCycle == 0):
                self.color = Color.RED
                waitedState = Color.YELLOW
                sleepTimeout = 7
            elif waitedState == Color.YELLOW and self.color == Color.RED:
                self.color = Color.YELLOW
                waitedState = Color.GREEN
                sleepTimeout = 2
            elif waitedState == Color.GREEN and self.color == Color.YELLOW:
                self.color = Color.GREEN
                waitedState = Color.RED
                sleepTimeout = 5
                currentCycle += 1
            elif self.color != waitedState:
                    raise Exception(f'Ожидаемый цвет {waitedState}. Текущий цвет {self.color}')
            else:
                raise Exception(f'Неизвестное состояние светофора {self.color}')
            print(f'Сингал светофора {self.color.value}')
            sleep(sleepTimeout)
trafficLight = TrafficLight()
trafficLight.running(1)