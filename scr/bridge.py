# Интерфейс устройства (Implementor)
class Device:
    def power_on(self):
        pass

    def power_off(self):
        pass

    def set_volume(self, volume):
        pass


# Конкретные устройства (Concrete Implementors)
class Television(Device):
    def __init__(self):
        self._is_on = False
        self._volume = 50

    def power_on(self):
        self._is_on = True
        print("Телевизор включен.")

    def power_off(self):
        self._is_on = False
        print("Телевизор выключен.")

    def set_volume(self, volume):
        self._volume = volume
        print(f"Громкость телевизора установлена на {self._volume}.")


class Radio(Device):
    def __init__(self):
        self._is_on = False
        self._volume = 30

    def power_on(self):
        self._is_on = True
        print("Радио включено.")

    def power_off(self):
        self._is_on = False
        print("Радио выключено.")

    def set_volume(self, volume):
        self._volume = volume
        print(f"Громкость радио установлена на {self._volume}.")


# Абстракция RemoteControl (Abstraction)
class RemoteControl:
    def __init__(self, device: Device):
        self.device = device

    def power_on(self):
        self.device.power_on()

    def power_off(self):
        self.device.power_off()

    def set_volume(self, volume):
        self.device.set_volume(volume)


# Расширенная абстракция для разных типов пультов (Refined Abstraction)
class IRRemoteControl(RemoteControl):
    def __init__(self, device: Device):
        super().__init__(device)
        print("Используется инфракрасный пульт.")


class BluetoothRemoteControl(RemoteControl):
    def __init__(self, device: Device):
        super().__init__(device)
        print("Используется Bluetooth пульт.")



# Создаем устройства
tv = Television()
radio = Radio()

# Инфракрасный пульт для телевизора
ir_remote_for_tv = IRRemoteControl(tv)
ir_remote_for_tv.power_on()
ir_remote_for_tv.set_volume(75)
ir_remote_for_tv.power_off()

print()

# Bluetooth пульт для радио
bt_remote_for_radio = BluetoothRemoteControl(radio)
bt_remote_for_radio.power_on()
bt_remote_for_radio.set_volume(40)
bt_remote_for_radio.power_off()
