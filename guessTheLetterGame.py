#!/usr/bin/python
import random

#This program is for better understanding for String randomness

def guessLetterCorrect():
    word='EVAPORATE'

    guessedWord='_'*len(word)

    word=list(word)

    guessedWord=list(guessedWord)

    listGuessedWord=[]

    while True:

        userIn=raw_input('Please guess a letter :')
        
        if userIn=="exit":
            break

        if userIn.upper() in listGuessedWord:
            userIn=''
            print 'You already guessed this once'

        elif userIn.upper() in word:
            for i in word:
                if i==userIn.upper():
                    index=word.index(userIn.upper())
                    guessedWord[index]=userIn.upper()
                    word[index]='_'
            print ''.join(guessedWord)

        elif userIn.upper() not in word:
            print 'Incorrect guess!'
            listGuessedWord.append(userIn.upper())

        if '_' not in guessedWord:
            print 'Wow! You guessed it correct!'
            break
        
if __name__=='__main__':
    print 'Welcome to Hangman game!\nGuess a word with guessing its letters one by one.\nHint: Word is a process to turn liquid into gas!\nEnter exit to quit the game'
    guessLetterCorrect()










