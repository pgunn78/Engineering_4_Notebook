#Writtin by Zane&Paxton
guessCount = 5
guessCountstr = str(guessCount)
lettersGuessed = ''
lettersGuessedstr = ''.join(str(e) for e in lettersGuessed)
word = input("Whats the Word (only lower case please): ")
print("\n" * 50)


while (guessCount > 0):
    lettersCorrect = 0
    gamestate = 0
    print("amount of guesses left ", guessCount)
    guess = input("Guess: ")
    if guess not in lettersGuessed:
        for letter in word:
            if guess == letter:
                lettersCorrect = lettersCorrect + 1
        if lettersCorrect > 0:
            print("Correct There is a " + guess)
        elif lettersCorrect == 0:
            print("wrong There is no " + guess)
            guessCount = guessCount - 1
        lettersGuessed = lettersGuessed + guess
    elif guess in lettersGuessed:
        print("you already guessed " + guess)
    for letter in word:
        if letter in lettersGuessed:
            print(letter, end = '')
        elif letter not in lettersGuessed:
            print("_", end = '')
            gamestate = gamestate + 1
    print("\n")
    if gamestate == 0:
        print("You Win!")
        break
    print("\n")
print("Game over")
