from enum import Enum
class ClothesTypes:
    COAT = 'пальто'
    COSTUME = 'костюм'
class Clothes:
    def __init__(self, name, typeClothes):
        self.__name = name
        self.__typeClothes = typeClothes
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, value):
        self.__name = value
    @property
    def typeClothes(self):
        return self.__typeClothes
    @typeClothes.setter
    def typeClothes(self, value):
        if isinstance(value, ClothesTypes):
            self.__typeClothes = value
    @property
    def growth(self):
        return self.__growth
    @growth.setter
    def growth(self, value):
        if isinstance(value, (int, float)):
            self.__growth = value
    def calcLength(self):
        raise Exception('Метод не определен')
class Coat(Clothes):
    def __init__(self, name, typeClothes, size):
        super().__init__(name, typeClothes)
        self.__size = size
    @property
    def size(self):
        return self.__size
    @size.setter
    def size(self, value):
        if isinstance(value, (int, float)):
            self.__size = value
    def calcLength(self):
        return self.size / 6.5 + 0.5
class Costume(Clothes):
    def __init__(self, name, typeClothes, growth):
        super().__init__(name, typeClothes)
        self.__growth = growth
    @property
    def size(self):
        return self.__size
    @size.setter
    def size(self, value):
        if isinstance(value, (int, float)):
            self.__size = value
    def calcLength(self):
        return self.__growth * 2 + 0.3
cloatheses = []
cloatheses.append(Costume('костюм 1', ClothesTypes.COSTUME, 6))
cloatheses.append(Costume('костюм 2', ClothesTypes.COSTUME, 7))
cloatheses.append(Coat('пальто 1', ClothesTypes.COAT, 12))
cloatheses.append(Coat('пальто 2', ClothesTypes.COAT, 4))
print (sum(cloathes.calcLength() for cloathes in cloatheses))