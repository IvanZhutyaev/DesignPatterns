from abc import ABC, abstractmethod

class State(ABC):
    @abstractmethod
    def press_play(self, player):
        pass
    
    @abstractmethod
    def press_pause(self, player):
        pass
    
    @abstractmethod
    def press_stop(self, player):
        pass

class PlayingState(State):
    def press_play(self, player):
        return "Уже воспроизводится"
    
    def press_pause(self, player):
        player.state = PausedState()
        return "Пауза"
    
    def press_stop(self, player):
        player.state = StoppedState()
        return "Остановлено"

class PausedState(State):
    def press_play(self, player):
        player.state = PlayingState()
        return "Продолжаем воспроизведение"
    
    def press_pause(self, player):
        return "Уже на паузе"
    
    def press_stop(self, player):
        player.state = StoppedState()
        return "Остановлено"

class StoppedState(State):
    def press_play(self, player):
        player.state = PlayingState()
        return "Начинаем воспроизведение"
    
    def press_pause(self, player):
        return "Сначала начните воспроизведение"
    
    def press_stop(self, player):
        return "Уже остановлено"

class MediaPlayer:
    def __init__(self):
        self.state = StoppedState()
    
    def press_play(self):
        return self.state.press_play(self)
    
    def press_pause(self):
        return self.state.press_pause(self)
    
    def press_stop(self):
        return self.state.press_stop(self)

# Использование
player = MediaPlayer()

print("Тестируем плеер:")
print("Старт:", player.press_play())      # Начинаем воспроизведение
print("Пауза:", player.press_pause())     # Пауза
print("Старт:", player.press_play())      # Продолжаем воспроизведение
print("Стоп:", player.press_stop())       # Остановлено
print("Пауза:", player.press_pause())     # Сначала начните воспроизведение
print("Старт:", player.press_play())      # Начинаем воспроизведение
print("Старт:", player.press_play())      # Уже воспроизводится