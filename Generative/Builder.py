class Computer:
    def __init__(self):
        self.cpu = None
        self.ram = None
        self.gpu = None
        self.storage = None

    def __str__(self):
        return f"Компьютер: CPU={self.cpu}, RAM={self.ram}, GPU={self.gpu}, Storage={self.storage}"


class ComputerBuilder:
    def __init__(self):
        self.computer = Computer()

    def set_cpu(self, cpu):
        self.computer.cpu = cpu
        return self

    def set_ram(self, ram):
        self.computer.ram = ram
        return self

    def set_gpu(self, gpu):
        self.computer.gpu = gpu
        return self

    def set_storage(self, storage):
        self.computer.storage = storage
        return self

    def build(self):
        return self.computer


# Директор (опционально, может определять типовые конфигурации)
class ComputerDirector:
    def build_gaming_pc(self, builder):
        return (builder
                .set_cpu("Intel i9")
                .set_ram("32GB")
                .set_gpu("NVIDIA RTX 4090")
                .set_storage("2TB SSD")
                .build())

    def build_office_pc(self, builder):
        return (builder
                .set_cpu("Intel i3")
                .set_ram("8GB")
                .set_gpu("Intel UHD")
                .set_storage("512GB SSD")
                .build())


# Использование
builder = ComputerBuilder()
director = ComputerDirector()

gaming_pc = director.build_gaming_pc(builder)
print("Игровой ПК:", gaming_pc)

# Или собираем вручную
office_builder = ComputerBuilder()
office_pc = (office_builder
             .set_cpu("AMD Ryzen 5")
             .set_ram("16GB")
             .set_gpu("NVIDIA GTX 1660")
             .set_storage("1TB SSD")
             .build())
print("Офисный ПК:", office_pc)