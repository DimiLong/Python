class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width
    def calc(self, mass, thicknessInCm):
        return self._width * self._length * mass * thicknessInCm / 100
road = Road(500, 20)
print(road.calc(25, 5), 'т')