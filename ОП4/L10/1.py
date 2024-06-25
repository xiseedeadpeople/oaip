class Item:
    def __init__(self, name, description):
        self._name = name
        self._description = description

    def info(self):
        return f"{self._name}: {self._description}"


class CraftingMaterial(Item):
    def __init__(self, name, description, amount):
        super().__init__(name, description)
        self._amount = amount

    def get_amount(self):
        return self._amount

    def decrease_amount(self, count):
        if self._amount >= count:
            self._amount -= count
            return True
        return False


class CraftingRecipe:
    def __init__(self, name, materials_needed, result_item):
        self._name = name
        self._materials_needed = materials_needed
        self._result_item = result_item

    def craft(self):
        can_craft = True
        for material, count in self._materials_needed.items():
            if material.get_amount() < count:
                can_craft = False
                break

        if can_craft:
            # Уменьшаем количество материалов
            for material, count in self._materials_needed.items():
                material.decrease_amount(count)

            # Создаем новый объект предмета по рецепту
            return self._result_item
        else:
            return None


# Пример использования
stone = CraftingMaterial("Stone", "A basic building material", 10)
stick = CraftingMaterial("Stick", "Used for crafting tools", 5)
sword = Item("Stone Sword", "A basic sword made of stone")

sword_recipe = CraftingRecipe("Stone Sword Recipe", {stone: 2, stick: 1}, sword)
crafted_item = sword_recipe.craft()

if crafted_item:
    print("Успешно создан предмет:", crafted_item.info())
else:
    print("Не удалось создать предмет из-за нехватки материалов.")
