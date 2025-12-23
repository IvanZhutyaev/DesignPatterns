class Captain:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.name = "Капитан Джек"
        return cls._instance

    def give_order(self):
        return f"{self.name}: Поднять паруса!"

# Использование
captain1 = Captain()
captain2 = Captain()

print(captain1.give_order())  # Капитан Джек: Поднять паруса!
print(captain1 is captain2)  # True - это один и тот же объект
print(f"ID капитана 1: {id(captain1)}")
print(f"ID капитана 2: {id(captain2)}")