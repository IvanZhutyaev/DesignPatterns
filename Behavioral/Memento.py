class GameState:
    """Состояние игры"""
    def __init__(self, level, health, inventory):
        self.level = level
        self.health = health
        self.inventory = inventory
    
    def __str__(self):
        return f"Уровень: {self.level}, Здоровье: {self.health}, Инвентарь: {self.inventory}"

class GameMemento:
    """Снимок состояния"""
    def __init__(self, state):
        self.state = state

class Game:
    """Оригинатор - игра"""
    def __init__(self):
        self.level = 1
        self.health = 100
        self.inventory = ["меч", "щит"]
    
    def play(self):
        # Игровой процесс меняет состояние
        self.level += 1
        self.health -= 10
        self.inventory.append(f"ключ_уровня_{self.level}")
        print(f"Игра: перешли на уровень {self.level}")
    
    def save(self) -> GameMemento:
        print(f"Игра: сохраняем состояние (уровень {self.level})")
        state = GameState(self.level, self.health, self.inventory.copy())
        return GameMemento(state)
    
    def load(self, memento: GameMemento):
        state = memento.state
        self.level = state.level
        self.health = state.health
        self.inventory = state.inventory.copy()
        print(f"Игра: загружаем состояние (уровень {self.level})")

class SaveManager:
    """Опекун - управляет снимками"""
    def __init__(self, game):
        self.game = game
        self.saves = []
    
    def save_game(self):
        self.saves.append(self.game.save())
    
    def load_game(self, index):
        if 0 <= index < len(self.saves):
            self.game.load(self.saves[index])
            return True
        return False
    
    def show_saves(self):
        print("\nСохраненные игры:")
        for i, save in enumerate(self.saves):
            print(f"  {i}: {save.state}")

# Использование
print("=== ИГРОВОЙ ПРОЦЕСС ===")
game = Game()
save_manager = SaveManager(game)

# Играем и сохраняемся
print("\nНачало игры:")
print(f"Текущее состояние: {GameState(game.level, game.health, game.inventory)}")

save_manager.save_game()  # Сохраняем начальное состояние

print("\nПроходим уровень 1:")
game.play()
save_manager.save_game()  # Сохраняем после 1 уровня

print("\nПроходим уровень 2:")
game.play()
game.play()  # Прошли сразу 2 уровня
save_manager.save_game()  # Сохраняем после 3 уровня

# Смотрим сохранения
save_manager.show_saves()

# Загружаем старое сохранение
print("\nОй, умерли! Загружаем сохранение 1:")
save_manager.load_game(1)
print(f"Текущее состояние: {GameState(game.level, game.health, game.inventory)}")