#Writtin by Zane&Paxton
guessCount = 5
guessCountstr = str(guessCount)
lettersGuessed = []
lettersGuessedstr = ''.join(str(e) for e in lettersGuessed)
sentence = input("Whats the Word (only lower case please): ")
print("\n" * 50)
sentence = sentence.split()
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

for word in sentence:
    if lettersGuessed in word:
        print(lettersGuessedstr, end = '')
    elif lettersGuessed not in word:
        print("_")
print(" ", end = '')
print("\n")

while (guessCount > 0):
    guess = input("Guess: ")
    if guess not in lettersGuessed:
        for word in sentence:
            if guess in word:
                print("Thats Right")
                print("there is a " + guess)
            elif guess not in word:
                guessCount-1
                print("no " + guess)
            lettersGuessed.append(guess)
    elif guess in lettersGuessed:
        print("you already guessed " + guess)

    
#def letterCheck (guess,sentence):

