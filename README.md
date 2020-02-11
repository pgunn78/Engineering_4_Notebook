# Engineering 4 Notebook

## Hello Raspberry Pi
Plug in the operating system into the side of the Pi. Then plug in hub and VGA cable to connect the monitor and pheripherals to the Pi
skip any updates to avoid long waits
open up the Terminal, and go to the Documents using the cd and ls command 
with the mikdr command make a directory called Scripts
in that directory make a file called hello_world openning using the nano command
in this file set a string equal to hello world which will be echoed
```
#!/bin/bash
str="Hello World!"
echo $str
```

save using the ctrl O and exit using ctrl X run the code with the bash command

## Hello Python
Open up Python using Thonny or Python 3
comment "written by Zane & Paxton" and "Dice Roller" at the top using #
run the code and save it as "Hello Python" 
import the random library this will enable the ability to generate sudo random numbers to use
set up a input called choice which will generate a random number between one and six (using the random library) every time enter is pressed, and while x is not pressed the code will keep running
```
#Automatic Dice Roller
#Written by Zane&Paxton
import random # the only library we need


choice = ''

print("press enter to roll dice press x then enter to exit program")

while(choice != "x"):
    print(random.randint(1,6))# generataes a randome number between one and six and print it
    choice = input() 
```

## Python Program - Calculator
Create a new program name it "Calculator"
create two input values, a and b, as floats
define a function named DoMath with three variables. a and b, the two input values and c which will tell us which of the five math functions to use
if c is equal to 1 than add a and b and set the sum equal to result else if c is equal to 2 than subtract b from a and set the difference equal to result continue for the next three math functions
have the function return a result as a string so that it can be printed
print each of the results from the function
```
#Writtin by Zane&Paxton

a = float(input('1st num: ')) 
b = float(input('2nd num: '))

def doMath(a,b,c): #Defines the DoMath function to find the sum, difference, product, quotient, and modulo between the two numbers
    if (c == 1):
        result = a+b
    elif (c == 2):
        result = a-b
    elif (c == 3):
        result = a*b
    elif (c == 4):
        result = round(a/b,2)
    elif (c == 5):
        result = a%b
    return str(result)

print("sum:\t\t" + doMath(a,b,1))  #prints out all the necesary values
print("Difference:\t\t" + doMath(a,b,2))
print("Product:\t\t" + doMath(a,b,3))
print("Quotient:\t\t" + doMath(a,b,4))
print("Modulo:\t\t" + doMath(a,b,5))
```
## Python Program - Quadratic Solver
Create a new program called "Quadratic_Solver"
have the program print a message asking the user to enter the coefficents a,b, and c to solve for the roots
create three inputs for each coefficent
define a function that will check how many real roots the quadratic equation has and if there are no roots than print "no real roots" and if there are roots find them through the quadratic formula and append them to a array and return that array
then print every element of that array
```
#Written By Zane&Paxton
import math
print("Quadratic Solver\nEnter the coefficients for ax^2 +bx +c = 0")

a = float(input('a: '))
b = float(input('b: '))
c = float(input('c: '))

def findRoots (a,b,c):
    Des = (b**2) - (4*a*c)
    roots = []
    if (Des < 0):
        print("no real roots")
    elif (Des >= 0):
        root1 = (-b+math.sqrt(Des))/(2*a)
        root2 = (-b-math.sqrt(Des))/(2*a)
    roots.append(root1)
    roots.append(root2)
    return roots

Quadratic = findRoots(a,b,c)
print("Here are your roots:")
for x in Quadratic:
    print(x)
```

## Hello Git
using the mkdir command in the terminal make a new directory named "Engineering_4_Nothebook
initiate github using the git init command
set up a github account using school username and password
set up email and name in the Raspberry Pi
open up the README for the Engineering 4 repository and add a breif description
git add the previous python assignments and commit
add remote server address to Pi
push to the origin master
and make a new directory named "Python"
move the previous assignments to this

## Git Forks and Clones
open git hub and click on the fork button in the Class_Accounts repository
now clone the repository with 
```
git clone https://github.com/<your GitHub Username>/Class_Accounts.git
```
open up the freshly cloned repository and edit the README
write name and intresting fact and save and close 
create a pull request by clicking on the new pull request button in github
and wait for doctor sheilds approval

## Python Program - Strings and Loops
create a new program
add a input named sentance and variable equal to sentance.split()
this will split the input the user puts in wherever there is a space
create a nested for statment that goes through every word in words and every letter in word printing the letter
on every space print a - by placing it outside the nested for loop
```
#Paxton&Zane

sentance = input("what do you want to say  ")
words = sentance.split()

for word in words:
    for letter in word:
        print(letter)
    print("-")
```
## Python Challendge - MSP
create a new program 
add a input named word this will be the word that player 2 must guess a empty array named letters guessed to keep track of letters already guessed by player 2 and a variable named guessCount which will end the game when it reaches 0
have a input named guess
if the letter in the guess is not already been guessed than using a for loop and if check to see if the letter guessed is equal to any of the letters in the word
have a counter that counts the letters guessed correctly and prints corrects if the guess is right
if the guess is wrong than subtract 1 from the guessCount
for every letter in the word check to see if the letter has already been guessed and if so print the letter and if the letter has not already been guess print a space and add 1 to gamestate which when all letters are guessed will equal zero and player 2 will have won
create a hangman graphic by printing lines and dashs everytime guess count goes down printing you lose if it reachs 0
```
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
        lettersGuessed = lettersGuessed + guess 
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
```

## GPIO pins - Python
Create a new program
import the RPI.GPIO library as the GPIO pin layout to allow the pin numbers to make mor sense
from the time library import the sleep function
set the GPIO pens to the BCM layout
set warnings equal to false (fake warnings tend to be thrown)
set GPIO pin 17 to an output
set up counter (for amount of times led has blinked)
make a while statment for when counter less than ten add the following underneath it
make the counter blink on for one second then off for one second
add plus one to counter at the end of the loop to allow it to count up properly
```
#Written by Paxton&Zane
import RPi.GPIO as GPIO
from time import sleep # all the librarys

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)# turns warnings off
GPIO.setup(17,GPIO.OUT)
count = 0 

while count < 10: # self explanitory just writes on and off ten times 
    GPIO.output(17, GPIO.HIGH)
    sleep(1)
    GPIO.output(17, GPIO.LOW)
    sleep(1)
    count = count + 1
```

## GPIO pins - SSH

## hello flask

Import flask library.
make a flask app called app.
make request to this directory spit out hello world.
make the code run the app.
make app visible to other computers using (0.0.0.0).

```
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hellow_world():
	return "hello world!"

if __name__ == "__main__":
	app.run(host="0.0.0.0", port=80)

```
