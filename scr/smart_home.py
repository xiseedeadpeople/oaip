class LightSystem:
    def __init__(self):
        self.status = False

    def turn_on(self):
        if not self.status:
            self.status = True
            print("свет включен")
        else:
            print("свет уже включен")

    def turn_off(self):
        if self.status:
            self.status = False
            print("свет выключен")
        else:
            print("свет уже выключен")


class TemperatureControlSystem:
    def __init__(self):
        self.temperature = 25

    def set(self, temperature):
        self.temperature = temperature
        print(f"установлена температура: {self.temperature}°C")

    def reset(self):
        print(f"температура сброшена ({self.temperature} -> 25°C)")
        self.temperature = 25


class SecuritySystem:
    def __init__(self):
        self.status = False

    def start(self):
        if not self.status:
            self.status = True
            print("система безопасности запущена.")
        else:
            print("система безопасности уже активнап")

    def stop(self):
        if self.status:
            self.status = False
            print("система безопасности остановлена")
        else:
            print("система безопасности уже остановлена.")


class SmartHomeFacade:
    def __init__(self):
        self.lighting = LightSystem()
        self.temperature = TemperatureControlSystem()
        self.security = SecuritySystem()

    def activate_home(self):
        print("\nбудим дом...")
        self.lighting.turn_on()
        self.temperature.set(22)
        self.security.start()
        print("умный дом запущен\n")

    def deactivate_home(self):
        print("\nвыключаем умный дом..")
        self.lighting.turn_off()
        self.temperature.reset()
        self.security.stop()
        print("умный дом остановлен\n")


smart_home = SmartHomeFacade()

smart_home.activate_home()
smart_home.temperature.set(24)
smart_home.deactivate_home()
