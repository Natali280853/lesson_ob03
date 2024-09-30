# Создайте базовый класс `Animal`, который будет содержать общие атрибуты (например, `name`, `age`) и методы (`make_sound()`, `eat()`) для всех животных.
# 2. Реализуйте наследование, создав подклассы `Bird`, `Mammal`, и `Reptile`, которые наследуют от класса `Animal`. Добавьте специфические атрибуты и переопределите методы, если требуется (например, различный звук для `make_sound()`).
# 3. Продемонстрируйте полиморфизм: создайте функцию `animal_sound(animals)`, которая принимает список животных и вызывает метод `make_sound()` для каждого животного.
# 4. Используйте композицию для создания класса `Zoo`, который будет содержать информацию о животных и сотрудниках. Должны быть методы для добавления животных и сотрудников в зоопарк.
# 5. Создайте классы для сотрудников, например, `ZooKeeper`, `Veterinarian`, которые могут иметь специфические методы (например, `feed_animal()` для `ZooKeeper` и `heal_animal()` для `Veterinarian`).

import pickle
import os

current_dir = os.getcwd()

#-----------------------------------------
#дополнительные функции|: сохранение информации о зоопарке в файл и возможность её загрузки, чтобы у зоопарка было "постоянное состояние" между запусками программы.
def save_zoo(zoo):
    file_path = os.path.join(current_dir, 'zoo_data.pickle')
    with open(file_path, 'wb') as file:
        pickle.dump(zoo, file)
    print("Информация о зоопарке сохранена.")


def load_zoo():
    try:
        file_path = os.path.join(current_dir, 'zoo_data.pickle')
        if os.path.getsize(file_path) > 0:
            with open(file_path, 'rb') as file:
                zoo = pickle.load(file)
                print("Информация о зоопарке загружена.")
                return zoo
        else:
            print("Файл с информацией о зоопарке пуст.")
            return {}
    except FileNotFoundError:
        print("Файл с информацией о зоопарке не найден.")
        return {}


class Animal():

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def make_sound(self):
        pass

    def eat(self):
        pass


class Bird(Animal):
    def __init__(self, name, age, wingspan):
        super().__init__(name, age)
        self.wingspan = wingspan

    def make_sound(self):
        print(f"{self.name} чирикает")

    def eat(self):
        print(f"{self.name} ест семена")


class Mammal(Animal):

    def __init__(self, name, age, fur):
        super().__init__(name, age)
        self.fur = fur

    def make_sound(self):
        print(f"{self.name} громко ревет")

    def eat(self):
        print(f"{self.name} ест траву")


class Reptile(Animal):
    def __init__(self, name, age, where_resides):
        super().__init__(name, age)
        self.where_resides = where_resides

    def make_sound(self):
        print(f"{self.name} шипит")

    def eat(self):
        print(f"{self.name} ест насекомых")


# Функция для демонстрации полиморфизма
def animal_sound(animals):
    for animal in animals:
        animal.make_sound()
        animal.eat()


animals = []

bird = Bird('Соловей', 11, "лес")
mammal = Mammal('Тигр', 5, 'шерсть')
reptile = Reptile('Ящерица', 20, "пустыня" )

animals.append(bird)
animals.append(mammal)
animals.append(reptile)

# for obj in animals:
#     print(obj.name, obj.age)
#     if hasattr(obj, 'make_sound'):
#         print(obj.name, obj.make_sound(), obj.eat())

animal_sound(animals)



class Zoo():
    def __init__(self):
        self.animals = []
        self.staff = []

    def add_animal(self, animal):
        self.animals.append(animal)

    def add_staff(self, staff):
        self.staff.append(staff)

class ZooKeeper():

    def feed_animal(self, animal):
        print(f"Смотритель кормит {animal.name}")

class Veterinarian ():

    def heal_animal(self, animal):
        print(f"Ветеринар лечит {animal.name}")


bird1 = Bird("Воробей", 1, "12 см")
mammal1 = Mammal("Лев", 5, "Brown")
reptile1 = Reptile("Змея", 2, "пустыня")

animals = [bird1, mammal1, reptile1]

animal_sound(animals)



#------------------------------------- Zoo

zoo = load_zoo()
if not zoo:
   zoo = Zoo()

zoo.add_animal(bird1)
zoo.add_animal(mammal1)
zoo.add_animal(reptile1)

zookeeper = ZooKeeper()
veterinarian = Veterinarian()

zoo.add_staff(zookeeper)
zoo.add_staff(veterinarian)

zookeeper.feed_animal(bird1)
veterinarian.heal_animal(mammal1)

save_zoo(zoo)
