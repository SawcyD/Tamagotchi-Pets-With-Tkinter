# Due: May 15th
#Group members:
# Read the instruction.md carefully
#Your code should be well-documented with comments and clear variable names
#Your code should handle errors gracefully
#Your code should be organized into different classes and modules for ease of maintenance and scalability

import tkinter
from tkinter import ttk, N, S, E, W
from PIL import ImageTk, Image

from pet import Pet
import pets

import random

# styling for the ui
Style = ttk.Style()

# emmanuel - created the styling for the ui elements
Style.configure('TFrame', background='#151515')
Style.configure('main.TFrame', padding='10 10 10 10')

Style.configure("TButton", padding=3, background="#202020", foreground='#171717', fill='#171717')

Style.configure('TLabel', background='#151515', font=('Sans Serif', 10), foreground='White')
Style.configure('stat.TLabel', padding='50 0 0 0')
Style.configure('value.TLabel', padding='0 0 50 0')

Style.configure('div.TFrame', background='#151515', width=500, height=25)

# Kevin - stat class for UI Stat elements which will hold the data for current pet stats
# Changeable stats using methods that tamper with the valuePointer attribute
class Stat:
    def __init__(self, parent: tkinter.Frame, name: str, default: any, position: int):
        self.title = ttk.Label(parent, text=name + " :", style='stat.TLabel')

        self.valuePointer = tkinter.StringVar()
        self.valuePointer.set(str(default))

        self.value = ttk.Label(parent, textvariable=self.valuePointer, style='value.TLabel')

        self.title.grid(column=1, row=position)
        self.value.grid(column=2, row=position)

    def set(self, newValue: any) -> None:
        self.valuePointer.set(str(newValue))

    def get(self) -> str:
        return self.valuePointer.get()

# Kevin - Action class for buttons that will be used to execute actions
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

        self.window = tkinter.Tk()

        self.window.title('Tamagotchi')
        self.window.geometry('500x600')

        self.window.columnconfigure(0, weight=1)

        self.mainFrame = ttk.Frame( style='main.TFrame')
        self.mainFrame.grid(column=0, row=0, sticky=(N, W, S, E))
        self.mainFrame.configure(padding="5 5 5 5")

        self.imagePath = self.pet.images.get(self.pet.getState(),  "Images/HappyDragon.png")
        self.Image = Image.open(self.imagePath)
        self.Image = self.Image.resize((200, 200), Image.LANCZOS)
        self.Image = ImageTk.PhotoImage(self.Image)



        self.petImage = tkinter.Label(self.mainFrame, image = self.Image)
        self.petImage.grid(column = 0, row = 0, columnspan = 3, sticky = (N))

        self.stats = []
        self.actions = []

        self.statsFrame = ttk.Frame(self.mainFrame, style = 'main.TFrame')
        self.statsFrame.grid(column = 0, row = 1, columnspan = 3, sticky = (N))

        self.name = self.createStat (self.statsFrame, 'Name', pet.name, 0)
        self.hunger = self.createStat (self.statsFrame, 'Hunger', pet.hunger, 1)
        self.happiness = self.createStat (self.statsFrame, 'Happiness', pet.happiness, 2)
        self.cleanliness = self.createStat (self.statsFrame, 'Cleanliness', pet.cleanliness, 3)
        self.health = self.createStat (self.statsFrame, 'Health', pet.health, 4)

        # div
        # ttk.Frame(self.mainFrame, height=25).grid(column=0, row=5)

        def Feed():
            try:
                self.pet.Feed()
                self.updateImage()
            except:
                print('You could not feed the pet')
            else:
                print('You fed the pet')

        self.actions_frame = ttk.Frame (self.mainFrame)
        self.actions_frame.grid (column = 0, row = 3 , columnspan = 3, sticky = (S))

        self.feed = self.createAction (self.actions_frame, 'Feed', lambda x: 3, 0)
        self.play = self.createAction (self.actions_frame, 'Player', lambda x: 3, 1)
        self.clean = self.createAction (self.actions_frame, 'Clean', lambda x: 3, 2)
        self.doctor = self.createAction (self.actions_frame, 'Doctor', lambda x: 1, 3)

        self.window.mainloop()

    def updateImage(self):
        mood = self.pet.getState()
        imageFile = self.pet.images.get(mood, "Images/HappyDragon.png")
        photo = tkinter.PhotoImage(file=imageFile)
        self.petImage.configure(image=photo)
        self.petImage.image = photo

    # Marissa - created this function to call stat and create stats
    def createStat (self, parent: tkinter.Frame, name: str, default: any, position: int = 0) -> Stat:
        _stat = Stat (parent, name, default, position)

        self.stats.append (_stat)

        return _stat

    # Marissa - created this function to call action and create buttons for actions
    def createAction(self, parent: tkinter.Frame, name: str, callback: callable, position: int) -> Action:
        _action = Action(parent, name, callback, position)

        self.actions.append(_action)

        return _action


if __name__ == '__main__':

    Tamagotchi(random.choice(pets.avaliablePets)())