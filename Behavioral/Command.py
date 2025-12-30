from abc import ABC, abstractmethod

# Команда
class Command(ABC):
    @abstractmethod
    def execute(self):
        pass
    
    @abstractmethod
    def undo(self):
        pass

class OrderCommand(Command):
    def __init__(self, receiver, dish, table):
        self.receiver = receiver
        self.dish = dish
        self.table = table
    
    def execute(self):
        return self.receiver.prepare(self.dish, self.table)
    
    def undo(self):
        return self.receiver.cancel(self.dish, self.table)

# Получатель
class Kitchen:
    def prepare(self, dish, table):
        return f"Готовим {dish} для стола {table}"
    
    def cancel(self, dish, table):
        return f"Отменяем {dish} для стола {table}"

# Инициатор
class Waiter:
    def __init__(self):
        self.commands = []
    
    def take_order(self, command):
        self.commands.append(command)
        result = command.execute()
        print(f"Официант: {result}")
        return result
    
    def cancel_last_order(self):
        if self.commands:
            command = self.commands.pop()
            result = command.undo()
            print(f"Официант: {result}")
            return result
        return "Нет заказов для отмены"

# Использование
kitchen = Kitchen()
waiter = Waiter()

# Создаем команды
order1 = OrderCommand(kitchen, "Стейк medium rare", 5)
order2 = OrderCommand(kitchen, "Салат Цезарь", 5)
order3 = OrderCommand(kitchen, "Вино красное", 5)

# Официант принимает заказы
waiter.take_order(order1)
waiter.take_order(order2)
waiter.take_order(order3)

print("\nКлиент передумал:")
waiter.cancel_last_order()
waiter.cancel_last_order()