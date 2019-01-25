Farm = []
class Animals:
  def __init__(self, name, weight, animal_type):
    self.name = name
    self.weight =  weight
    self.animal_type = animal_type
    Farm.append(self)
  def __gt__(self, other):
    return self.weight > other.weight
  def __add__(self, other):
    return (Animals("Скот", self.weight + other.weight), "Скот")
  def feed(self):
    return print(self.animal_type, self.name, "покормлен(a)")
  def take_care(self):
    return print(self.name, "обслужен")
  def make_a_sound(self):
    return print(self.name + ", подай голос")

class Giving_milk(Animals):
  def __init__(self, name, weight, animal_type = "Корова"):
    super().__init__(name, weight, animal_type)
  def take_care(self):
    return print(self.animal_type, self.name, "подоена")

class Cows(Giving_milk):
  def __init__(self, name, weight, animal_type = "Корова"):
    super().__init__(name, weight, animal_type)
  def make_a_sound(self):
    return print(self.name + ', скажи "Му-у!"')

class Goats(Giving_milk):
  def __init__(self, name, weight, animal_type = "Коза"):
    super().__init__(name, weight, animal_type)
  def make_a_sound(self):
    return print(self.name, ', скажи "Ме-е!"')

class Sheep(Animals):
  def __init__(self, name, weight, animal_type = "Овца"):
    super().__init__(name, weight, animal_type)
  def take_care(self):
    return print(self.animal_type, self.name, "пострижена")
  def make_a_sound(self):
    return print(self.name, ', скажи "Бе-е!"')

class Birds(Animals):
  def __init__(self, name, weight, animal_type = "Корова"):
    super().__init__(name, weight, animal_type)
  def take_care(self):
    return print(self.animal_type, self.name + ": яйца собраны")

class Geese(Birds):
  def __init__(self, name, weight, animal_type = "Гусь"):
    super().__init__(name, weight, animal_type)
  def make_a_sound(self):
    return print(self.name, ', скажи "Га-га-га!"')

class Chicken(Birds):
  def __init__(self, name, weight, animal_type = "Курица"):
    super().__init__(name, weight, animal_type)
  def make_a_sound(self):
    return print(self.name, ', скажи "Ко-ко-ко!"')

class Ducks(Birds):
  def __init__(self, name, weight, animal_type = "Утка"):
    super().__init__(name, weight, animal_type)
  def make_a_sound(self):
    return print(self.name, ', скажи "Кря-кря!"')

cow1 = Cows("Манька", 630, "Корова")
goat1 = Goats("Рога", 120, "Коза")
goat2 = Goats("Копыта", 110, "Коза")
sheep1 = Sheep("Барашек", 250, "Овца")
sheep2 = Sheep("Кудрявый", 270, "Овца")
goose1 = Geese("Серый", 15, "Гусь")
goose2 = Geese("Белый", 12, "Гусь")
chicken1 = Chicken("Ко-ко", 3, "Курица")
chicken1 = Chicken("Кукареку", 2, "Курица")
Duck1 = Ducks("Кряква", 7, "Утка")
cattle = Animals("Скот", 0, "Скот")

for animal in Farm:
  animal.feed()
  animal.take_care()

#к сожалению, не нашел более изящного способа обработать сразу все экземпляры класса
cattle_weight = 0
for animal in Farm:
  cattle_weight = cattle_weight + animal.weight
print("Общий вес скота:", cattle_weight)

for animal in Farm:  
  if animal > cattle : cattle = animal
print("Самое крупное животное -", cattle.animal_type,  cattle.name, "весом", cattle.weight, "кг")
