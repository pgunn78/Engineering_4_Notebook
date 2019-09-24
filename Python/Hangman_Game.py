#Writtin by Zane&Paxton
guessCount = 5
lettersGuessed = []
lettersGuessedstr = ''.join(str(e) for e in lettersGuessed)
sentence = input("Whats the Word (only lower case please): ")
print("\n" * 50)
sentence = sentence.split()

while (guessCount > 0):
    guess = input("Guess: ")
    if guess not in lettersGuessed:
        for word in sentence:
            if guess in word:
                print("Thats Right")
                print("there is a " + guess)
            elif guess not in word:
                guessCount - 1
                print("no " + guess)
            lettersGuessed.append(guess)
    elif guess in lettersGuessed:
        print("you already guessed " + guess)
    for word in sentence:
        if lettersGuessedstr in word:
            print(lettersGuessedstr, end = '')
        elif lettersGuessed not in word:
            print("_")
    print(" ", end = '')
print("\n")
    
#def letterCheck (guess,sentence):


if (guessCount == 5):
    print("amount of guesses left " + guessCount)
if (guessCount == 4):
    print("amount of guesses left " + guessCount)
if (guessCount == 3):
    print("amount of guesses left " + guessCount)
if (guessCount == 2):
    print("amount of guesses left " + guessCount)
if (guessCount == 1):
    print("amount of guesses left " + guessCount)
if (guessCount == 0):
    print("\n" * 50)
    print("You Lose")