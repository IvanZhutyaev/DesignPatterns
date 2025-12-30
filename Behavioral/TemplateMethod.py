from abc import ABC, abstractmethod

class BeverageRecipe(ABC):
    """Шаблонный метод"""
    def prepare(self):
        steps = [
            self.boil_water(),
            self.add_main_ingredient(),
            self.add_extras(),
            self.stir()
        ]
        return " -> ".join(steps)
    
    def boil_water(self):
        return "Вскипятить воду"
    
    @abstractmethod
    def add_main_ingredient(self):
        pass
        
    @abstractmethod
    def add_extras(self):
        pass
    
    def stir(self):
        return "Перемешать"

class TeaRecipe(BeverageRecipe):
    def add_main_ingredient(self):
        return "Добавить чайные листья"
    
    def add_extras(self):
        return "Добавить лимон"

class CoffeeRecipe(BeverageRecipe):
    def add_main_ingredient(self):
        return "Добавить кофейные зерна"
    
    def add_extras(self):
        return "Добавить сахар и молоко"

# Использование
tea = TeaRecipe()
coffee = CoffeeRecipe()

print("Приготовление чая:")
print(tea.prepare())

print("\nПриготовление кофе:")
print(coffee.prepare())