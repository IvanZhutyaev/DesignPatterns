class Airplane:
    def __init__(self, name, mediator=None):
        self.name = name
        self.mediator = mediator
    
    def send_message(self, message):
        print(f"{self.name}: {message}")
        if self.mediator:
            self.mediator.notify(self, message)
    
    def receive_message(self, message):
        print(f"{self.name} получил: {message}")

class AirTrafficControl:
    """Посредник"""
    def __init__(self):
        self.airplanes = []
    
    def register(self, airplane):
        self.airplanes.append(airplane)
        airplane.mediator = self
    
    def notify(self, sender, message):
        for airplane in self.airplanes:
            if airplane != sender:
                airplane.receive_message(f"От {sender.name}: {message}")

# Использование
control_tower = AirTrafficControl()

airplane1 = Airplane("Боинг-737")
airplane2 = Airplane("Аэробус A320")
airplane3 = Airplane("Суперджет-100")

control_tower.register(airplane1)
control_tower.register(airplane2)
control_tower.register(airplane3)

print("Связь между самолетами через диспетчера:")
airplane1.send_message("Запрашиваю разрешение на взлет")
airplane2.send_message("Занимаю полосу 25L")
airplane3.send_message("Выруливаю к гейту")