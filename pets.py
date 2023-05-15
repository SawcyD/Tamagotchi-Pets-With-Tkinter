from pet import Pet

class Dragon(Pet):
    def __init__(self):
        super().__init__(
            'Dragon',
            hunger = 50,
            happiness = 50,
            cleanliness = 25,
            hungerRate = 15,
            happinessRate = 10,
            dirtyRate = 10
        )

        self.hunger = 50
        self.happiness = 50
        self.cleanliness = 25
        self.hungerRate = 15
        self.happinessRate = 10
        self.dirtyRate = 10

        self.images  = {
            "Happy": "Images/HappyDragon.png",
            "Sad": "Images/SadDragon.png",
            "Dirty": "Images/DirtyDragon.png",
            "Sick": "Images/SickDragon.png",
            "Hungry": "Images/HungryDragon.png"
        }

class Monster(Pet):
    def __init__(self):
        super().__init__(
            'Monster',
            hunger = 35,
            happiness = 10,
            cleanliness = 15,
            hungerRate = 25,
            happinessRate = 10
        )

        self.hunger = 35
        self.happiness = 10
        self.cleanliness = 15
        self.hungerRate = 25
        self.happinessRate = 10

        self.images = {
            "Happy": "Images/HappyMonster.png",
            "Sad": "Images/SadMonster.png",
            "Dirty": "Images/DirtyMonster.png",
            "Sick": "Images/SickMonster.png",
            "Hungry": "Images/HungryMonster.png"
        }

class Fluffycat(Pet):
    def __init__(self):
        super().__init__(
            'Fluffycat',
            hunger = 15,
            happiness = 80,
            cleanliness = 15,
            ditryRate = 30
        )

        self.hunger = 15
        self.happiness = 80
        self.cleanliness = 15
        self.dirtyRate = 30

        self.images = {
            "Happy": "Images/FCHappy.png",
            "Sad": "Images/FCSad.png",
            "Dirty": "Images/FCDirty.png",
            "Sick": "Images/FCSick.png",
            "Hungry": "Images/FCHungry.png"
        }

    def Fluff(self) -> None:
        print('you fluffed the cat')

class Kitten(Pet):
    def __init__(self):
        super().__init__(
            'Kitten',
            hunger = 15,
            happiness = 90,
            cleanliness = 60,
            hungerRate = 2
        )

        self.hunger = 15
        self.happiness = 90
        self.cleanliness = 60
        self.hungerRate = 2

        self.images = {
            "Happy": "Images/HappyDragon.png",
            "Sad": "Images/SadDragon.png",
            "Dirty": "Images/DirtyDragon.png",
            "Sick": "Images/SickDragon.png",
            "Hungry": "Images/HungryDragon.png"
        }

    def pet(self) -> None:
        print('you pet the kitten')

avaliablePets = [Dragon, Monster, Fluffycat, Kitten]