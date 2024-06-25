class Weapon:
    def __init__(self, name, damage, weapon_range, weight):
        self.name = name
        self.damage = damage
        self.weapon_range = weapon_range
        self.weight = weight

    def info(self):
        return f"{self.name}: Damage {self.damage}, Range {self.weapon_range}, Weight {self.weight}"


# Класс Firearm (Огнестрельное оружие)
class Firearm(Weapon):
    def __init__(self, name, damage, weapon_range, weight, ammo_type, magazine_capacity, fire_mode):
        super().__init__(name, damage, weapon_range, weight)
        self.ammo_type = ammo_type
        self.magazine_capacity = magazine_capacity
        self.fire_mode = fire_mode

    def info(self):
        return f"{super().info()}, Ammo Type {self.ammo_type}, Magazine Capacity {self.magazine_capacity}, Fire Mode {self.fire_mode}"


# Класс MeleeWeapon (Холодное оружие)
class MeleeWeapon(Weapon):
    def __init__(self, name, damage, weapon_range, weight, material, hand_usage, durability):
        super().__init__(name, damage, weapon_range, weight)
        self.material = material
        self.hand_usage = hand_usage
        self.durability = durability

    def info(self):
        return f"{super().info()}, Material {self.material}, Hand Usage {self.hand_usage}, Durability {self.durability}"


# Пример использования
if __name__ == "__main__":
    # Создание оружия
    pistol = Firearm("Pistol", 30, 50, 1.5, "9mm", 12, "Single")
    sword = MeleeWeapon("Sword", 50, 2, 3.0, "Steel", "Single-handed", 100)

    # Вывод информации о каждом виде оружия
    print(pistol.info())
    print(sword.info())
