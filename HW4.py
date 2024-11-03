import random

class Garden:
    def __init__(self, size):
        self.size = size  # Размер сада
        self.plants = []  # Список растений в саду

    def plant(self, plant):
        if len(self.plants) < self.size:
            self.plants.append(plant)
            print(f"{plant.name} посажен(а) в сад.")
        else:
            print("Сад полон, нельзя посадить больше растений.")

    def water(self):
        for plant in self.plants:
            plant.water()
        print("Все растения в саду политы.")

    def harvest(self):
        for plant in self.plants:
            if plant.is_ready_to_harvest():
                plant.harvest()
            else:
                print(f"{plant.name} еще не готов(а) к сбору урожая.")


class Plant:
    def __init__(self, name, growth_time):
        self.name = name
        self.growth_time = growth_time  # Время роста в днях
        self.days_passed = 0  # Сколько дней прошло с момента посадки

    def water(self):
        print(f"{self.name} поливается.")

    def grow(self):
        self.days_passed += 1
        print(f"{self.name} растет... Прошло {self.days_passed} дней.")

    def is_ready_to_harvest(self):
        return self.days_passed >= self.growth_time

    def harvest(self):
        print(f"{self.name} собран(а)!") 
        # Можно добавить удаление растения из сада, если нужно.


# Пример использования
garden = Garden(size=3)

plant1 = Plant("Помидор", growth_time=5)
plant2 = Plant("Огурец", growth_time=3)
plant3 = Plant("Перец", growth_time=4)

garden.plant(plant1)
garden.plant(plant2)
garden.plant(plant3)

# Симуляция роста растений
for day in range(6):  # Симулируем 6 дней
    print(f"\nДень {day + 1}:")
    garden.water()
    for plant in garden.plants:
        plant.grow()
    garden.harvest()
