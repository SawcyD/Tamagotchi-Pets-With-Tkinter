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


    # Marisssa - feed function to feed pet
    def Feed(self) -> None or str:
        if self.hunger <= 0:
            return print('your pet is not hungry')

        self.hunger = max(self.hunger - 25, 0)

    # lee - function to play with pet
    def Play(self) -> None or str:
        if self.happiness >= 100:
            return print('your pet is already happy, come back and play another time')

        self.happiness = min(self.happiness + 5, 100)

    # lee - function to clean pet
    def Clean(self) -> None or str:
        if self.cleanliness >= 100:
            return 'your pet is already clean, you can only clean it when it is dirty'

        self.cleanliness = min(self.cleanliness + 15, 100)

    # Marisssa - function to doctor/heal pet
    def Doctor(self) -> None or str:
        if self.health >= 100:
            return print('your pet is already healthy, you can only doctor it when it is low health')

        self.health = min(self.health + 25, 100)


    # Kevin
    # function to execute a cycle of stat decrease/increase
    def executeCycle(self) -> None:
        self.hunger = min(self.hunger + self.hungerRate, 100)
        self.happiness = max(self.happiness - self.happinessRate, 0)
        self.cleanliness = max(self.cleanliness - self.dirtyRate, 0)

        # will only decrease health if there is a stat that is too low
        if self.getNeeds() != 'Nothing':
            self.health = max(self.cleanliness - self.healthRate, 0)


    # emmanyel - getState function returns the state of the pet according to its stats
    def getState(self) -> str:
        if self.hunger >= 80:
            return 'Starving'
        elif self.hunger >= 60:
            return 'Hungry'

        if self.happiness <= 10:
            return 'Very sad'
        elif self.happiness <= 25:
            return 'sad'

        if self.cleanliness <= 10:
            return 'Very dirty'
        elif self.cleanliness <= 25:
            return 'dirty'

        if self.health <= 10:
            return 'Very sick'
        elif self.health <= 25:
            return 'sick'

        return 'Healthy'

    # emmanuel - getNeeds function returns all the needs of the current pet according to stats
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