from abc import ABC, abstractmethod


# Реализация
class Device(ABC):
    @abstractmethod
    def power_on(self):
        pass

    @abstractmethod
    def power_off(self):
        pass

    @abstractmethod
    def set_volume(self, level):
        pass


class TV(Device):
    def power_on(self):
        return "Телевизор включен"

    def power_off(self):
        return "Телевизор выключен"

    def set_volume(self, level):
        return f"Громкость телевизора: {level}"


class Radio(Device):
    def power_on(self):
        return "Радио включено"

    def power_off(self):
        return "Радио выключено"

    def set_volume(self, level):
        return f"Громкость радио: {level}"


# Абстракция
class Remote(ABC):
    def __init__(self, device):
        self.device = device

    @abstractmethod
    def toggle_power(self):
        pass

    def volume_up(self):
        return self.device.set_volume("+")


class BasicRemote(Remote):
    def __init__(self, device):
        super().__init__(device)
        self.powered_on = False

    def toggle_power(self):
        if not self.powered_on:
            self.powered_on = True
            return self.device.power_on()
        else:
            self.powered_on = False
            return self.device.power_off()


class AdvancedRemote(Remote):
    def __init__(self, device):
        super().__init__(device)
        self.powered_on = False
        self.volume_level = 10

    def toggle_power(self):
        if not self.powered_on:
            self.powered_on = True
            return f"{self.device.power_on()} (плавный запуск)"
        else:
            self.powered_on = False
            return f"{self.device.power_off()} (плановое отключение)"

    def volume_up(self):
        self.volume_level += 2
        return self.device.set_volume(self.volume_level)

    def mute(self):
        return self.device.set_volume(0)


# Использование
tv = TV()
radio = Radio()

basic_tv_remote = BasicRemote(tv)
advanced_radio_remote = AdvancedRemote(radio)

print(basic_tv_remote.toggle_power())  # Телевизор включен
print(basic_tv_remote.volume_up())  # Громкость телевизора: +

print("\n" + advanced_radio_remote.toggle_power())  # Радио включено (плавный запуск)
print(advanced_radio_remote.volume_up())  # Громкость радио: 12
print(advanced_radio_remote.mute())  # Громкость радио: 0