from abc import ABC, abstractmethod
# Абстрактные продукты
class Chair(ABC):
    @abstractmethod
    def sit(self):
        pass
class Table(ABC):
    @abstractmethod
    def use(self):
        pass
# Современная мебель
class ModernChair(Chair):
    def sit(self):
        return "Сижу на современном стуле"
class ModernTable(Table):
    def use(self):
        return "Использую современный стол"
# Классическая мебель
class ClassicChair(Chair):
    def sit(self):
        return "Сижу на классическом стуле"
class ClassicTable(Table):
    def use(self):
        return "Использую классический стол"
# Абстрактная фабрика
class FurnitureFactory(ABC):
    @abstractmethod
    def create_chair(self) -> Chair:
        pass
    @abstractmethod
    def create_table(self) -> Table:
        pass
# Конкретные фабрики
class ModernFurnitureFactory(FurnitureFactory):
    def create_chair(self):
        return ModernChair()
    def create_table(self):
        return ModernTable()

class ClassicFurnitureFactory(FurnitureFactory):
    def create_chair(self):
        return ClassicChair()
    def create_table(self):
        return ClassicTable()
# Использование
def create_furniture_set(factory: FurnitureFactory):
    chair = factory.create_chair()
    table = factory.create_table()
    return f"{chair.sit()}\n{table.use()}"

modern_factory = ModernFurnitureFactory()
classic_factory = ClassicFurnitureFactory()

print("Современный гарнитур:")
print(create_furniture_set(modern_factory))

print("\nКлассический гарнитур:")
print(create_furniture_set(classic_factory))