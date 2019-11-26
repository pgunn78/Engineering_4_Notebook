#Automatic Dice Roller
#Written by Zane&Paxton
import random # the only library we need


choice = ''

print("press enter to roll dice press x then enter to exit program")

while(choice != "x"):
    print(random.randint(1,6))
    choice = input() # generataes a randome number between one and six
