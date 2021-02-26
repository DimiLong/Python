class Cell:
    def __init__(self, count):
        self.count = count
    @property
    def count(self):
        return self.__count
    @count.setter
    def count(self, value):
        if isinstance(value, int):
            self.__count = value
        else:
            raise Exception('Указаный параметр не целое число \'count\'')
    def __checkIsCell(self, cell):
        if not isinstance(cell, Cell):
            raise Exception('Параметр не является типом \'Cell\'')
    def __add__(self, cell):
        self.__checkIsCell(cell)
        return Cell(int(self.count + cell.count))
    def __sub__(self, cell):
        self.__checkIsCell(cell)
        return Cell(int(self.count - cell.count)) if self.count - cell.count > 0 \
            else print('Количество клеток не может быть нулевым или отрицательным')
    def __mul__(self, cell):
        self.__checkIsCell(cell)
        return Cell(int(self.count * cell.count))
    def __truediv__(self, cell):
        return Cell(int(round(self.count // cell.count)))
    def make_order(self, cellInRow):
        row = ''
        for i in range(int(self.count / cellInRow)):
            row += f'{"*" * cellInRow} \\n'
        row += f'{"*" * (self.count % cellInRow)}'
        return row
cell1 = Cell(18)
cell2 = Cell(14)
print('Сложение: ', (cell1 + cell2).count)
print('Вычитание: ', (cell1 - cell2).count)
print('Умножение: ', (cell1 * cell2).count)
print('Деление: ', (cell1 / cell2).count)
print(cell1.make_order(4))
