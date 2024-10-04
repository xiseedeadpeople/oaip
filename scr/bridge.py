class Device:
    def power_on(self):
        pass

    def power_off(self):
        pass

    def set_volume(self, volume):
        pass


class Television(Device):
    def __init__(self):
        self.status = False
        self._volume = 50

    def power_on(self):
        self.status = True
        print('телевизор включен')

    def power_off(self):
        self.status = False
        print('телевизор выключен')

    def set_volume(self, volume):
        self._volume = volume
        print(f'громкость телевизора установлена на {self._volume}')


class Radio(Device):
    def __init__(self):
        self.status = False
        self._volume = 30

    def power_on(self):
        self.status = True
        print('радио включено')

    def power_off(self):
        self.status = False
        print('радио выключено')

    def set_volume(self, volume):
        self._volume = volume
        print(f'громкость радио установлена на {self._volume}')


class RemoteControl:
    def __init__(self, device: Device):
        self.device = device

    def power_on(self):
        self.device.power_on()

    def power_off(self):
        self.device.power_off()

    def set_volume(self, volume):
        self.device.set_volume(volume)


class IRRemoteControl(RemoteControl):
    def __init__(self, device: Device):
        super().__init__(device)
        print('используется обычный пульт')


class BluetoothRemoteControl(RemoteControl):
    def __init__(self, device: Device):
        super().__init__(device)
        print('используется bluetooth пульт')


tv = Television()
radio = Radio()

# tv
ir_remote_for_tv = IRRemoteControl(tv)
ir_remote_for_tv.power_on()
ir_remote_for_tv.set_volume(75)
ir_remote_for_tv.power_off()

print()

# radio
bt_remote_for_radio = BluetoothRemoteControl(radio)
bt_remote_for_radio.power_on()
bt_remote_for_radio.set_volume(40)
bt_remote_for_radio.power_off()
