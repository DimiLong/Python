class Stationery:
    def __init__(self, title):
        self.title = title
    def draw(self):
        print('Запуск отрисовки.')
class Pen(Stationery):
    def __init__(self, title):
        super().__init__(title)
    def draw(self):
        print('Рисуем ручку.')
class Pencil(Stationery):
    def __init__(self, title):
        super().__init__(title)
    def draw(self):
        print('Рисуем карандаш.')
class Handle(Stationery):
    def __init__(self, title):
        super().__init__(title)
    def draw(self):
        print('Рисуем маркер.')
stationery = Stationery('Канцелярский предмет')
pen = Pen('Канцелярский предмет')
pencil = Pencil('Канцелярский предмет')
handle = Handle('Канцелярский предмет')
stationery.draw()
pen.draw()
pencil.draw()
handle.draw()