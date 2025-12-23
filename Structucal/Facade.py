class Grinder:
    def grind_beans(self):
        return "Зерна помолоты"


class WaterHeater:
    def heat_water(self):
        return "Вода нагрета"


class BrewUnit:
    def brew(self):
        return "Кофе заварен"


class MilkFrother:
    def froth_milk(self):
        return "Молоко вспенено"


class CoffeeMachineFacade:
    """Фасад для сложной системы кофемашины"""

    def __init__(self):
        self.grinder = Grinder()
        self.water_heater = WaterHeater()
        self.brew_unit = BrewUnit()
        self.milk_frother = MilkFrother()

    def make_espresso(self):
        steps = [
            self.grinder.grind_beans(),
            self.water_heater.heat_water(),
            self.brew_unit.brew()
        ]
        return "Эспрессо готов: " + " -> ".join(steps)

    def make_cappuccino(self):
        steps = [
            self.grinder.grind_beans(),
            self.water_heater.heat_water(),
            self.brew_unit.brew(),
            self.milk_frother.froth_milk()
        ]
        return "Капучино готов: " + " -> ".join(steps)

    def make_americano(self):
        steps = [
            self.grinder.grind_beans(),
            self.water_heater.heat_water(),
            self.brew_unit.brew(),
            "Добавлена горячая вода"
        ]
        return "Американо готов: " + " -> ".join(steps)


# Использование
coffee_machine = CoffeeMachineFacade()

print("Нажимаем кнопки на фасаде:")
print(coffee_machine.make_espresso())
print("\n" + coffee_machine.make_cappuccino())
print("\n" + coffee_machine.make_americano())