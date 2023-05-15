import tkinter
from tkinter import ttk, N, S, E, W
from PIL import ImageTk, Image

from pet import Pet
import pets

import random

# # styling for the ui
# Style = ttk.Style()
#
# # emmanuel - created the styling for the ui elements
# Style.configure('TFrame', background='#151515')
# Style.configure('main.TFrame', padding='10 10 10 10')
#
# Style.configure("TButton", padding=3, background="#202020", foreground='#171717', fill='#171717')
#
# Style.configure('TLabel', background='#151515', font=('Sans Serif', 10), foreground='White')
# Style.configure('stat.TLabel', padding='50 0 0 0')
# Style.configure('value.TLabel', padding='0 0 50 0')
#
# Style.configure('div.TFrame', background='#151515', width=500, height=25)

# stat class for UI Stat elements which will hold the data for current pet stats
# Changeable stats using methods that tamper with the valuePointer attribute
class Stat:
    def __init__(self, parent: tkinter.Frame, name: str, default: any, position: int):
        self.title = tkinter.Label(parent, text=name + " :")
        self.title.configure(background='#1e1e1e', font=('Sans Serif', 10), foreground='White')

        self.valuePointer = tkinter.StringVar()
        self.valuePointer.set(str(default))

        self.value = tkinter.Label(parent, textvariable=self.valuePointer)
        self.value.configure(background='#1e1e1e', font=('Sans Serif', 10), foreground='White')

        self.title.grid(column=1, row=position, columnspan=1, sticky=(tkinter.W, tkinter.E))
        self.value.grid(column=2, row=position, sticky=(tkinter.W, tkinter.E))

        tkinter.Frame(parent, background='#1e1e1e').grid(column=0, row=position, sticky=(tkinter.W, tkinter.E))


    def set(self, newValue: any) -> None:
        self.valuePointer.set(str(newValue))

    def get(self) -> str:
        return self.valuePointer.get()

# Action class for buttons that will be used to execute actions
# Includes callback variable to apply specific behavior to each button/Action instanced
class Action:
    def __init__(self, parent: tkinter.Frame, name: str, callback: callable, position: int):
        self.callback = callback

        self.button = tkinter.Button(parent, text=name)
        self.button.configure(padx=3, pady=3, background='#1C1C1C', foreground='white')
        self.button.bind('<Button-1>', callback)
        self.button.grid(column=position, row=6)

    def setCallback(self, callback: callable) -> None:
        self.callback = callback

        self.button.unbind('<Button-1>')
        self.button.bind('<Button-1>', callback)

class Tamagotchi:
    def __init__(self, pet):
        self.pet = pet

        # Tkinter window instance
        self.window = tkinter.Tk()

        self.window.title('Tamagotchi')
        self.window.geometry('500x600')
        self.window.configure(background='#1e1e1e')

        self.window.columnconfigure(0, weight=1)

        # Main frame
        self.mainFrame = tkinter.Frame(self.window, background='#1e1e1e')
        self.mainFrame.grid(column=0, row=0, sticky=(N, W, S, E))
        self.mainFrame.configure(padx=5, pady=5)

        # imaging
        self.petImage = None
        self.updateImage()

        # Arrays
        self.stats = []
        self.actions = []

        # status
        self.statusString = tkinter.StringVar()

        self.updateStatus()

        self.statusLabel = tkinter.Label(self.mainFrame, textvariable=self.statusString, background='#1e1e1e', foreground='white')
        self.statusLabel.grid(column=0, row=1, columnspan=3, sticky=(W, E))

        # stats
        self.statsFrame = ttk.Frame(self.mainFrame, style = 'main.TFrame')
        self.statsFrame.grid(column = 0, row = 2, columnspan = 3, sticky = (N))

        self.name = self.createStat (self.statsFrame, 'Name', pet.name, 0)
        self.hunger = self.createStat (self.statsFrame, 'Hunger', pet.hunger, 1)
        self.happiness = self.createStat (self.statsFrame, 'Happiness', pet.happiness, 2)
        self.cleanliness = self.createStat (self.statsFrame, 'Cleanliness', pet.cleanliness, 3)
        self.health = self.createStat (self.statsFrame, 'Health', pet.health, 4)

        # needs label
        self.needString = tkinter.StringVar()
        self.updateNeeds()

        tkinter.Label(self.mainFrame, text='Needs:', background='#1e1e1e', foreground='red').grid(column=0, row=5, columnspan=2, sticky=(tkinter.E))

        self.needLabel = tkinter.Label(self.mainFrame, textvariable=self.needString, background='#1e1e1e', foreground='#808080')
        self.needLabel.grid(column=2, row=5, columnspan=1, sticky=(tkinter.W))

        # Notifications
        self.notificationString = tkinter.StringVar()

        self.notificationLabel = tkinter.Label(self.mainFrame, textvariable=self.notificationString, background='#1e1e1e', foreground='white')
        self.notificationLabel.grid(column=0, row=6, columnspan=3, sticky=(tkinter.W, tkinter.E), pady=(10, 5))

        # internal functions to handle action events
        def Feed(event: tkinter.Event) -> None:
            try:
                self.pet.Feed()
            except Exception as reason:
                self.alert(str(reason), 2000)
            else:
                self.info('You fed your pet.', 2000)
                self.update()

        def Play(event: tkinter.Event) -> None:
            try:
                self.pet.Play()
            except Exception as reason:
                self.alert(str(reason), 2000)
            else:
                self.info('You played with your pet.', 2000)
                self.update()

        def Clean(event: tkinter.Event) -> None:
            try:
                self.pet.Clean()
            except Exception as reason:
                self.alert(str(reason), 2000)
            else:
                self.info('You cleaned your pet.', 2000)
                self.update()

        def Doctor(event: tkinter.Event) -> None:
            try:
                self.pet.Doctor()
            except Exception as reason:
                self.alert(str(reason), 2000)
            else:
                self.info('You took your pet to the doctor.', 2000)
                self.update()

        self.actions_frame = ttk.Frame (self.mainFrame)
        self.actions_frame.grid (column = 0, row = 7 , columnspan = 3, sticky = (S))

        self.feed = self.createAction (self.actions_frame, 'Feed', Feed, 0)
        self.play = self.createAction (self.actions_frame, 'Play', Play, 1)
        self.clean = self.createAction (self.actions_frame, 'Clean', Clean, 2)
        self.doctor = self.createAction (self.actions_frame, 'Doctor', Doctor, 3)

        self.cycle()
        self.window.mainloop()

    # method updates image on screen based off the pet's stats/status
    def updateImage(self) -> None:
        mood = self.pet.getSimpleState()

        self.Image = Image.open(f"Images/{self.pet.name}/{mood}.png")
        self.Image = self.Image.resize((200, 200), Image.LANCZOS)
        self.Image = ImageTk.PhotoImage(self.Image)

        if not self.petImage:
            self.petImage = tkinter.Label(self.mainFrame, image=self.Image)
            self.petImage.grid(column=0, row=0, columnspan=3, sticky=(N), pady=(0, 5))

        self.petImage.configure(image=self.Image)

    # Updates stats on screen
    def updateStats(self) -> None:
        self.hunger.set(self.pet.hunger)
        self.happiness.set(self.pet.happiness)
        self.cleanliness.set(self.pet.cleanliness)
        self.health.set(self.pet.health)

    # updates needs
    def updateNeeds(self) -> None:
        self.needString.set(self.pet.getNeeds())

    # updates the status
    def updateStatus(self) -> None:
        self.statusString.set(self.pet.getState())


    # all update function to call other update functions to minimize code repeatability
    def update(self):
        self.updateStats()
        self.updateImage()
        self.updateNeeds()
        self.updateStatus()

    # created this function to call stat and create stats
    def createStat (self, parent: tkinter.Frame, name: str, default: any, position: int = 0) -> Stat:
        _stat = Stat (parent, name, default, position)

        self.stats.append (_stat)

        return _stat

    # created this function to call action and create buttons for actions
    def createAction(self, parent: tkinter.Frame, name: str, callback: callable, position: int) -> Action:
        _action = Action(parent, name, callback, position)

        self.actions.append(_action)

        return _action

    # alert on screen
    def alert(self, text: str, delay: int = 1000) -> None:
        self.notificationLabel.configure(foreground='red')
        self.notificationString.set(text)

        self.window.after(delay, lambda: self.notificationString.set(''))

    # warn on screen
    def warn(self, text: str, delay: int = 1000) -> None:
        self.notificationLabel.configure(foreground='orange')
        self.notificationString.set(text)

        self.window.after(delay, lambda: self.notificationString.set(''))

    # display info on screen
    def info(self, text: str, delay: int = 1000) -> None:
        self.notificationLabel.configure(foreground='white')
        self.notificationString.set(text)

        self.window.after(delay, lambda: self.notificationString.set(''))

    # recursive cycle that lowers stats over time
    def cycle(self):
        self.pet.executeCycle()
        self.update()

        if self.pet.health <= 0:
            self.alert('Your pet has died.', 6000)

            return self.window.after(5000, self.window.destroy)

        self.window.after(60000, self.cycle)



if __name__ == '__main__':
    Tamagotchi(random.choice(pets.avaliablePets)())
