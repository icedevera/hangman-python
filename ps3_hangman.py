# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    numcorrect=0
    for letter in secretWord:
        for character in lettersGuessed:
            if letter == character:
                numcorrect += 1
                break
    return len(secretWord) == numcorrect



def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    guessedWord=''
    if lettersGuessed != []:
        for letter in secretWord:
            for character in lettersGuessed:
                if letter == character:
                    guessedWord += character
                    break
                elif character == lettersGuessed[len(lettersGuessed)-1]:
                    guessedWord += ' _ '
    else:
        for i in secretWord:
            guessedWord += ' _ '
    return guessedWord



def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    for letters in lettersGuessed:
        if letters in alphabet:
            alphabet.remove(letters)
    return ''.join(alphabet)
    

def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    guesses=8
    lettersGuessed = []
    letterguess=''
    guessedalready=''
    guessinlowercase=''
    print('Welcome to the game, Hangman!')
    print('I am thinking of a word that is ' + str(len(secretWord)) + ' letters long.')
    
    while guesses > -1:
        if guesses == 0:
            print ('-------------')
            print('Sorry, you ran out of guesses. The word was ' + secretWord + '.')
            break
        elif isWordGuessed(secretWord, lettersGuessed) == True:
            print ('-------------')
            print('Congratulations, you won!')
            break
        else:
            print ('-------------')
            print ('You have ' + str(guesses) + ' guesses left.')
            print ('Available letters: ' + getAvailableLetters(lettersGuessed))
            letterguess = input('Please guess a letter: ')
            guessinlowercase = letterguess.lower()
            if guessinlowercase in guessedalready:
                print("Oops! You've already guessed that letter: " + getGuessedWord(secretWord,lettersGuessed))
                guessedalready += guessinlowercase
            elif guessinlowercase in secretWord:
                lettersGuessed.append(guessinlowercase)
                print('Good guess: ' + getGuessedWord(secretWord,lettersGuessed))
                guessedalready += guessinlowercase
            else:
                print('Oops! That letter is not in my word: ' + getGuessedWord(secretWord,lettersGuessed))
                guesses -= 1
                lettersGuessed.append(guessinlowercase)
                guessedalready += guessinlowercase
                
            


# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

# secretWord = chooseWord(wordlist).lower()
# hangman(secretWord)
