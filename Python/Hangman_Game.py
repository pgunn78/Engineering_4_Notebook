#Writtin by Zane&Paxton
guessCount = 5
guessCountstr = str(guessCount)
lettersGuessed = ''
lettersGuessedstr = ''.join(str(e) for e in lettersGuessed)
word = input("Whats the Word (only lower case please): ")
print("\n" * 50)


if (guessCount == 5):
    print("amount of guesses left " + guessCountstr)
if (guessCount == 4):
    print("amount of guesses left " + guessCountstr)
if (guessCount == 3):
    print("amount of guesses left " + guessCountstr)
if (guessCount == 2):
    print("amount of guesses left " + guessCountstr)
if (guessCount == 1):
    print("amount of guesses left " + guessCountstr)
if (guessCount == 0):
    print("\n" * 50)
    print("You Lose")


while (guessCount > 0):
    gamestate = 0
    guess = input("Guess: ")
    if guess not in lettersGuessed:
        for letter in word:
            if letter in lettersGuessed:
                print("Thats Right")
                print("there is a " + guess)
            elif letter not in lettersGuessed:
                guessCount = guessCount-1
                print("no " + guess)
        lettersGuessed = lettersGuessed + guess
    elif guess in lettersGuessed:
        print("you already guessed " + guess)
    for letter in word:
        if letter in lettersGuessed:
            print(letter, end = '')
        elif letter not in lettersGuessed:
            print("_", end = '')
    print("\n")