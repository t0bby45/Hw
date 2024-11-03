import random

class Pet:
    def __init__(self, name, species):
        self.name = name
        self.species = species  # "cat" или "dog"
        self.happiness = 100
        self.hunger = 0
        self.energy = 100

    def feed(self):
        if self.hunger > 0:
            food_amount = random.randint(10, 30)
            self.hunger -= food_amount
            self.hunger = max(self.hunger, 0)
            print(f"{self.name} покушал(а) и стал(а) менее голодным(ой). Голод: {self.hunger}")
        else:
            print(f"{self.name} не голоден(на).")

    def play(self):
        if self.energy > 10:
            self.happiness += 20
            self.energy -= 10
            self.hunger += 5
            print(f"{self.name} играет и радуется! Счастье: {self.happiness}, Энергия: {self.energy}, Голод: {self.hunger}")
        else:
            print(f"{self.name} слишком уставший(ая) для игры.")

    def rest(self):
        self.energy += 20
        self.energy = min(self.energy, 100)
        print(f"{self.name} отдыхает. Энергия: {self.energy}")

    def live_day(self):
        print(f"\n{self.name} начинает день.")
        action = random.choice(["feed", "play", "rest"])
        if action == "feed":
            self.feed()
        elif action == "play":
            self.play()
        elif action == "rest":
            self.rest()

        # Увеличиваем голод и уменьшаем счастье со временем
        self.hunger += 10
        self.happiness -= 5
        self.happiness = max(self.happiness, 0)
        print(f"К концу дня: Счастье: {self.happiness}, Голод: {self.hunger}")


class Human:
    def __init__(self, name):
        self.name = name
        self.pet = None
        self.job = None

    def adopt_pet(self, pet):
        self.pet = pet
        print(f"{self.name} приютил(а) питомца {self.pet.name}.")

    def take_care_of_pet(self):
        if self.pet:
            print(f"{self.name} заботится о питомце {self.pet.name}.")
            action = random.choice(["feed", "play"])
            if action == "feed":
                self.pet.feed()
            elif action == "play":
                self.pet.play()
        else:
            print(f"{self.name} не имеет питомца.")

    def work(self):
        if self.job:
            earned_money = random.randint(50, 100)
            print(f"{self.name} работает и зарабатывает {earned_money} денег.")
        else:
            print(f"{self.name} безработный.")

    def set_job(self, job):
        self.job = job
        print(f"{self.name} теперь работает как {self.job}.")

    def live_day(self):
        print(f"\n{self.name} начинает день.")
        self.take_care_of_pet()
        self.work()
        if self.pet:
            self.pet.live_day()


# Пример использования
human = Human("Анна")
pet = Pet("Мурка", "cat")

human.adopt_pet(pet)
human.set_job("программист")

for _ in range(7):  # Имитируем жизнь в течение недели
    human.live_day()
