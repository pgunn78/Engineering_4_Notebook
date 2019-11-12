#Writtin by Zane&Paxton
import RPi.GPIO as GPIO
from time import sleep
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(17,GPIO.OUT)
GPIO.output(17, GPIO.HIGH)

guessCount = 6
lettersGuessed = ''
word = input("Whats the Word (only lower case please): ")
print("\n" * 50)


while (guessCount > 0):
    gameState = 0
    lettersCorrect = 0
    print("amount of guesses left ", + guessCount)
    if guessCount == 6:
        print("   ------  \n   |    |  \n   |       \n   |       \n   |       \n-------      ")
    if guessCount == 5:
        print("   ------  \n   |    |  \n   |    0  \n   |       \n   |       \n-------      ")
    if guessCount == 4:
        print("   ------  \n   |    |  \n   |    0  \n   |    |  \n   |       \n-------      ")
    if guessCount == 3:
        print("   ------  \n   |    |  \n   |    0  \n   |    |\ \n   |       \n-------      ")
    if guessCount == 2:
        print("   ------  \n   |    |  \n   |    0  \n   |   /|\ \n   |       \n-------      ")
    if guessCount == 1:
        print("   ------  \n   |    |  \n   |    0  \n   |   /|\ \n   |   /   \n-------      ")
    
    guess = input("Guess: ")
    if guess not in lettersGuessed:
        for letter in word:
            if letter in guess:
                lettersCorrect = lettersCorrect + 1
        if lettersCorrect > 0:
                print("correct there is a " + guess)
        elif lettersCorrect == 0:
                print("wrong there is no " + guess)
                guessCount = guessCount - 1
        lettersGuessed = lettersGuessed + guess
    elif guess in lettersGuessed:
        print("you already guessed " + guess)
    for letter in word:
        if letter in lettersGuessed:
            print(letter, end = '')
        elif letter not in lettersGuessed:
            print("_", end = '')
            gameState = gameState + 1
    print("\n")
    if gameState == 0:
        print("You Win!")
        break

print("\n" * 50)
if guessCount == 0:
        print("   ------  \n   |    |  \n   |    0  \n   |   /|\ \n   |   / \ \n-------      ")
if guessCount == 0:
    print("You Lose")
    for i in range(0,10):
        GPIO.output(17, GPIO.LOW)
        sleep(0.05)
        GPIO.output(17, GPIO.HIGH)
        sleep(.1)