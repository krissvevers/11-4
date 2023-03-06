import random

words = [ "viens", "divi", "tris", "cits" ]
inGame = False
totalLives = 5
word = random.choice(words)
guessedWord = list("_" for _ in word) # ["_", "_", "_"]
print(word)
#print("".join(guessedWord))
#for _ in word:
    #guessedWord += "_"
while (totalLives > 0 and not "".join(guessedWord) == word):  
    inp = input("Ievade (burts): ")
    if (len(inp) < 1): continue
    inp = inp[0]

    didGuessLetter = False
    for aaa in range(0,  len(guessedWord)):
        if word[aaa] == inp:
            guessedWord[aaa] = inp
            didGuessLetter = True

    if not didGuessLetter:
        totalLives -= 1

    #print(didGuessLetter)
    print("".join(guessedWord))

if (totalLives > 0):
    print("Uzvara")
else:
    print("Zaudēja")