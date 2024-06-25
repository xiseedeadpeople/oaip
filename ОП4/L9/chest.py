class Chest:
    def __init__(self, capacity):
        self.capacity = capacity  # вместимость сундука
        self.items = []  # список предметов в сундуке

    def add_item(self, item):
        """Добавить предмет в сундук."""
        if len(self.items) < self.capacity:
            self.items.append(item)
            print(f"{item} добавлен в сундук.")
        else:
            print("Сундук полон, предмет не может быть добавлен.")

    def remove_item(self, item):
        """Убрать предмет из сундука."""
        if item in self.items:
            self.items.remove(item)
            print(f"{item} удален из сундука.")
        else:
            print(f"{item} не найден в сундуке.")

    def view_items(self):
        """Просмотреть содержимое сундука."""
        if self.items:
            print("Содержимое сундука:")
            for item in self.items:
                print(f"- {item}")
        else:
            print("Сундук пуст.")
