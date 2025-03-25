from random import choice, randint
from string import ascii_letters
class Die:
    def __init__(self, sides=6):
        self.sides = sides
    def roll_die(self):
        return randint(1, self.sides)

dice_6 = Die()

for _ in range(10):
    print(dice_6.roll_die())
print("----------------------")
dice_20 = Die(20)
for _ in range(10):
    print(dice_20.roll_die())

lottery = []
for _ in range(10):
    lottery.append(randint(0, 9))
for _ in range(5):
    lottery.append(choice(ascii_letters))
res = ""
for _ in range(4):
    res += str(choice(lottery))
print(f"Person with the {res} wins the lottery")