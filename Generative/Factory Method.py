from abc import ABC, abstractmethod

# Абстрактный дом
class House(ABC):
    @abstractmethod
    def build(self):
        pass

# Конкретные дома
class WoodHouse(House):
    def build(self):
        return "Деревянный дом построен"

class BrickHouse(House):
    def build(self):
        return "Кирпичный дом построен"

# Строительная компания (Фабрика)
class ConstructionCompany:
    def create_house(self, house_type):
        if house_type == "wood":
            return WoodHouse()
        elif house_type == "brick":
            return BrickHouse()
        else:
            raise ValueError("Неизвестный тип дома")

# Использование
company = ConstructionCompany()
house1 = company.create_house("wood")
house2 = company.create_house("brick")

print(house1.build())  # Деревянный дом построен
print(house2.build())  # Кирпичный дом построен