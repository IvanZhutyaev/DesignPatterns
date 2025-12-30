from abc import ABC, abstractmethod

class RouteStrategy(ABC):
    @abstractmethod
    def build_route(self, start, end):
        pass

class FastestRouteStrategy(RouteStrategy):
    def build_route(self, start, end):
        return f"Самый быстрый маршрут из {start} в {end}: 50 минут"

class ShortestRouteStrategy(RouteStrategy):
    def build_route(self, start, end):
        return f"Самый короткий маршрут из {start} в {end}: 30 км"

class ScenicRouteStrategy(RouteStrategy):
    def build_route(self, start, end):
        return f"Живописный маршрут из {start} в {end}: через горы и озера"

class Navigator:
    def __init__(self, strategy=None):
        self.strategy = strategy
    
    def set_strategy(self, strategy):
        self.strategy = strategy
    
    def build_route(self, start, end):
        if self.strategy:
            return self.strategy.build_route(start, end)
        return "Выберите стратегию маршрута"

# Использование
navigator = Navigator()

# Меняем стратегии на лету
navigator.set_strategy(FastestRouteStrategy())
print(navigator.build_route("Дом", "Работа"))

navigator.set_strategy(ShortestRouteStrategy())
print(navigator.build_route("Дом", "Работа"))

navigator.set_strategy(ScenicRouteStrategy())
print(navigator.build_route("Дом", "Работа"))