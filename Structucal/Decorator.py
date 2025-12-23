class Person:
    """Базовый компонент"""

    def __init__(self, name):
        self.name = name

    def wear(self):
        return f"{self.name}"


class ClothingDecorator:
    """Базовый декоратор"""

    def __init__(self, person):
        self.person = person

    def wear(self):
        return self.person.wear()


class TShirtDecorator(ClothingDecorator):
    def wear(self):
        return f"{self.person.wear()} | 👕 Футболка"


class JacketDecorator(ClothingDecorator):
    def wear(self):
        return f"{self.person.wear()} | 🧥 Пиджак"


class RaincoatDecorator(ClothingDecorator):
    def wear(self):
        return f"{self.person.wear()} | 🧥 Плащ"


# Использование
person = Person("Иван")

# Одеваем человека слоями
dressed_person = TShirtDecorator(person)
print("Футболка:", dressed_person.wear())

dressed_person = JacketDecorator(dressed_person)
print("+ Пиджак:", dressed_person.wear())

dressed_person = RaincoatDecorator(dressed_person)
print("+ Плащ:", dressed_person.wear())

# Или цепочкой
print("\nИли сразу цепочкой:")
fully_dressed = RaincoatDecorator(JacketDecorator(TShirtDecorator(Person("Пашенция"))))
print(fully_dressed.wear())