class Pet:
    def __init__(self, name: str, **stats):
        self.name = name

        # basic stats
        self.hunger = stats.get('hunger', 25)
        self.happiness = stats.get('happiness', 30)
        self.cleanliness = stats.get('cleanliness', 50)
        self.health = stats.get('health', 100)

        # rates
        self.hungerRate = stats.get('hungerRate', 5)
        self.happinessRate = stats.get('happinessRate', 10)
        self.dirtyRate = stats.get('dirtyRate', 5)
        self.healthRate = stats.get('healthRate', 2)


    # feed function to feed pet
    def Feed(self) -> None:
        if self.hunger <= 0:
            raise Exception('Your pet is not hungry.')

        self.hunger = max(self.hunger - 25, 0)

    # function to play with pet
    def Play(self) -> None:
        if self.happiness >= 100:
            raise Exception('Your pet is already happy. Come back and play later.')

        self.happiness = min(self.happiness + 5, 100)

    # function to clean pet
    def Clean(self) -> None:
        if self.cleanliness >= 100:
            raise Exception('Your pet is already clean.')

        self.cleanliness = min(self.cleanliness + 15, 100)

    # function to doctor/heal pet
    def Doctor(self) -> None:
        if self.health >= 100:
            raise Exception('Your pet is healthy. Doctor is not needed.')

        self.health = min(self.health + 25, 100)


    # function to execute a cycle of stat decrease/increase
    def executeCycle(self) -> None:
        self.hunger = min(self.hunger + self.hungerRate, 100)
        self.happiness = max(self.happiness - self.happinessRate, 0)
        self.cleanliness = max(self.cleanliness - self.dirtyRate, 0)

        # will only decrease health if there is a stat that is too low
        if self.getNeeds() != 'Nothing':
            self.health = max(self.health - self.healthRate, 0)


    # getState function returns the state of the pet according to its stats
    def getState(self) -> str:
        if self.hunger >= 80:
            return 'Starving'
        elif self.hunger >= 60:
            return 'Hungry'

        if self.happiness <= 10:
            return 'Very sad'
        elif self.happiness <= 25:
            return 'Sad'

        if self.cleanliness <= 10:
            return 'Very dirty'
        elif self.cleanliness <= 25:
            return 'Dirty'

        if self.health <= 10:
            return 'Very sick'
        elif self.health <= 25:
            return 'Sick'

        return 'Healthy'

    # gets simple state for image retrival
    def getSimpleState(self):
        if self.health <= 25:
            return 'Hungry'
        elif self.happiness <= 25:
            return 'Sad'
        elif self.cleanliness <= 25:
            return 'Dirty'
        elif self.hunger >= 60:
            return 'Sick'

        return 'Happy'

    # getNeeds function returns all the needs of the current pet according to stats
    def getNeeds(self) -> str:
        needs = ''

        if self.hunger >= 60:
            needs += 'Food, '

        if self.happiness <= 25:
            needs += 'Joy, '

        if self.cleanliness <= 25:
            needs += 'Hygiene, '

        if self.health <= 25:
            needs += 'Doctor  '

        if not needs:
            return 'Nothing'

        return needs[:-2]
