import random

#constant variable in caps
HANGMAN_PICS = ['''
    +---+
        |
        |
        |
       === ''','''
    +---+
    o   |
        |
        |
       === ''','''
    +---+
    o   |
    |   |
        |
       === ''','''
    +---+
    o   |
   /|   |
        |
       === ''','''
    +---+
    o   |
   /|\  |
        |
       === ''','''
    +---+
    o   |
   /|\  |
     \ |
       === ''','''
    +---+
    o   |
   /|\  |
   / \  |
       === ''']

words = 'tiger leopard bear bat cokatoo eagle crocodile python cobra orangutan monkey fish'.split()

def getRandomWord(wordList):
    wordIndex = random.randint(0, len(wordList)-1)
    return wordList[wordIndex]

def displayHangman(missedLetters, correctLetters, secretWord):
    print(HANGMAN_PICS[len(missedLetters)])
    print()

    print('Missed Leters: ', end =' ')
    for letter in missedLetters:
        print(letter, end = ' ')
    print()

    blanks = '_' * len(secretWord)

    for i in range (len(secretWord)):
        if secretWord[i] in correctLetters:
            blanks = blanks[:i] + secretWord[i] + blanks[i+1:]

    for letter in blanks:
        print(letter, end = ' ')
    print()

def getGuess(alreadyGuessed):
    while True:
        print("Guess a letter")
        guess = input()
        guess = guess.lower()
        if len(guess) !=1:
            print('please guess one letter at a time')
        elif guess in alreadyGuessed:
            print('you have already guessed that letter')
        elif guess not in 'abcdefghijklmnopqrstuvwxyz':
            print('please enter a letter')
        else:
            return guess

def playAgain():
    print('Do you want to play again? ')
    return input.lower().startswith('y')

print ('H A N G M A N')
missedLetters = ' '
correctLetters = ' '
secretWord = getRandomWord(words)
gameIsDone = False

while True:
    displayHangman(missedLetters, correctLetters, secretWord)

    #player enters letter
    guess = getGuess(missedLetters + correctLetters)

    if guess in secretWord:
        correctLetters = correctLetters + guess

        #check if the player won
        foundAllLetters = True
        for i in range(len(secretWord)):
            if secretWord[i] not in correctLetters:
                foundAllLetters = False
                break

        if foundAllLetters:
            print ("You guessed it, the secret word is"+ secretWord+ ".")
            gameIsDone = True

    else:
        missedLetters = missedLetters + guess

        if len(missedLetters) == len(HANGMAN_PICS) - 1:
            displayHangman(missedLetters, correctLetters, secretWord)
            print ("You've run out of guesses, the secret word was", secretWord)
            gameIsDone = True

        if gameIsDone:
            if playAgain():
                missedLetters = " "
                correctLetters = " "
                gameIsDone = False
                secretWord = getRandomWord(words)
            else:
                break
