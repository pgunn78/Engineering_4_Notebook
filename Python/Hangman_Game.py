#Writtin by Zane&Paxton
guessCount = 6
lettersGuessed = ''
word = input("Whats the Word (only lower case please): ")
print("\n" * 50) # allows you to type in a word then clears the screen


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
        print("   ------  \n   |    |  \n   |    0  \n   |   /|\ \n   |   /   \n-------      ")# draws the hangeman 
    
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
        lettersGuessed = lettersGuessed + guess # breaks the words into leters then checks to see if your guess is one of those 
    elif guess in lettersGuessed:
        print("you already guessed " + guess) # if you already guessed a letter wont let you do it again
    for letter in word:
        if letter in lettersGuessed:
            print(letter, end = '')
        elif letter not in lettersGuessed:
            print("_", end = '')
            gameState = gameState + 1 
    print("\n")
    if gameState == 0:
        print("You Win!")
        break # above decied if you win or lose then breaks itself off if you lost

print("\n" * 50)
if guessCount == 0:
        print("   ------  \n   |    |  \n   |    0  \n   |   /|\ \n   |   / \ \n-------      ")
if guessCount == 0:
    print("You Lose") # the losing screen
