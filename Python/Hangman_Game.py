#Writtin by Zane&Paxton
guessCount = 5
lettersGuessed = ''
word = input("Whats the Word (only lower case please): ")
print("\n" * 50)

while (guessCount > 0):
    gameState = 0
    lettersCorrect = 0
    print("amount of guesses left ", + guessCount)
    guess = input("Guess: ")
    if guess not in lettersGuessed:
        for letter in word:
            gameState = gameState + 1
            if letter in guess:
                lettersCorrect = lettersCorrect + 1
                gameState = gameState - 1
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
    print("\n")
    if gameState == 0:
        print("You Win!")
        break
    print("\n")
    
if guessCount == 0:
    print("You Lose")