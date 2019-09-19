#Writtin by Zane&Paxton
guessCount = 5
lettersGuessed = []
sentence = input("Whats the Word: ")
print("\n" * 50)
sentence = sentence.split()

while (guessCount != 0):
    for word in sentence:
        for letter in word:
            print("_", end = '')
        print(" ", end = '')
print("\n")
guess = input("Guess: ")

def letterCheck (guess,sentence):
    for letter in sentence:
        if (guess == letter):
            print("thats right")
            print("there is"+ amountLetters + guess)
        #letter you guessed correct and how many of that letter there are
        elif (guess != letter):
             guessCount - 1
             print("no " + guess)
        lettersGuessed.append(guess)

if (guessCount == 5):
    print("amount of guesses left" + guessCount)
if (guessCount == 4):
    print("amount of guesses left" + guessCount)
if (guessCount == 3):
    print("amount of guesses left" + guessCount)
if (guessCount == 2):
    print("amount of guesses left" + guessCount)
if (guessCount == 1):
    print("amount of guesses left" + guessCount)
if (guessCount == 0):
    print("\n" * 50)
    print("You Lose")