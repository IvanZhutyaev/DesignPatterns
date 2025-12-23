# Европейская вилка
class EuropeanPlug:
    def connect_european(self):
        return "Подключено к европейской розетке"


# Американская розетка
class AmericanSocket:
    def connect_american(self):
        return "Готов к американской вилке"


# Адаптер
class SocketAdapter:
    def __init__(self, socket):
        self.socket = socket

    def connect(self):
        # Адаптер преобразует интерфейс
        result = self.socket.connect_american()
        return f"Адаптер: {result} -> Преобразовано для европейской вилки"


# Использование
european_plug = EuropeanPlug()
american_socket = AmericanSocket()

# Без адаптера несовместимы
print("Европейская вилка:", european_plug.connect_european())
print("Американская розетка:", american_socket.connect_american())

# Используем адаптер
adapter = SocketAdapter(american_socket)
print("Через адаптер:", adapter.connect())