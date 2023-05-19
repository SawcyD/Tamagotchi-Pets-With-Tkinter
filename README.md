# Tamagotchi Pet Simulator

This python project is a simple, text-based Tamagotchi pet simulator. In this game, you can take care of a virtual pet of your choosing.

## Prerequisites
Ensure that you have the following installed:
* Python 3.6 or later
* tkinter package
* PIL package

## Game Setup
The game uses the following modules:

* `pets` module - this contains the classes for the available pets, namely `Dragon`, `Monster`, and `Fluffycat`. Each pet has different initial stats and rates of stat change. 

* `tamagotchi` module - this contains the `Tamagotchi` class which creates the user interface for the game and handles the game logic.

## How to Run
Run the `tamagotchi` module to start the game. The game randomly selects one of the available pets at startup.

```python
python tamagotchi.py
```

## Game Play
The game uses a graphical user interface created with tkinter. 

The main game screen displays the following:
* The pet's image which changes based on the pet's current state.
* The pet's current stats: hunger, happiness, cleanliness, and health.
* The pet's needs based on the current stats.
* The current status of the pet.

You can interact with your pet using the available actions: `Feed`, `Play`, `Clean`, and `Doctor`.

- `Feed` - Decreases the pet's hunger. Cannot be used if the pet is not hungry.
- `Play` - Increases the pet's happiness. Cannot be used if the pet is already happy.
- `Clean` - Increases the pet's cleanliness. Cannot be used if the pet is already clean.
- `Doctor` - Increases the pet's health. Cannot be used if the pet is already healthy.

Each action updates the pet's status and the game screen is updated to reflect the changes.

## Game Cycle
The game uses a cycle system where the pet's stats change over time. After each cycle, the pet's hunger increases, its happiness and cleanliness decrease. If the pet's hunger is high and cleanliness is low, the pet's health will decrease. 

If the pet's health reaches 0, the pet dies and the game ends.

Enjoy playing!
