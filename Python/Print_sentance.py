#Paxton&Zane

sentance = input("what do you want to say  ")
words = sentance.split()

for word in words:
    for letter in word:
        print(letter)
    print("-")