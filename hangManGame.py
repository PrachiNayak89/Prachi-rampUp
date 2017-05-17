#!/usr/bin/python
import random

#This program contains the Hamgman game logic combining the pick a word and guess a letter programs
def printHang(n):
    gal = [['---- '],
           ['|  | '],
           ['|    '],
           ['|    '],
           ['|    ']]
    if n < 6:
        gal[2] = ['|  o ']
    if n < 5:
        gal[3] = ['| /  ']
    if n < 4:
        gal[3] = ['| / \\']
    if n < 3:
        gal[3] = ['| /|\\']
    if n < 2:
        gal[4] = ['| /  ']
    if n < 1:
        gal[4] = ['| / \\']
    for i in gal:
	print(''.join(i))

def pickAword():
	listToStore=[]
	with open("sowpodsDictionary.txt","r") as fileToRead:
    		line=fileToRead.readline().strip()
    		while line:
        		words=line
        		listToStore.append(words)
        		line=fileToRead.readline().strip()

    	randomWord=random.choice(listToStore)
	return randomWord;

def guessALetter(word):
	guessedWord='_'*len(word)

    	word=list(word)

    	guessedWord=list(guessedWord)

    	listGuessedWord=[]
        count=6

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
                        count-=1
                        printHang(count)

        	elif userIn.upper() not in word:
            		print 'Incorrect guess!'
            		listGuessedWord.append(userIn.upper())
                        count-=1
                        printHang(count)
                
        	if '_' not in guessedWord:
            		print 'Wow! You guessed it correct!'
            		break
                
                if count==0:
                    print 'Game over! You loss!'
                    break


if __name__=="__main__":
    answer="yes"
    while True and answer!='no' or answer!='No':
        if answer=="no" or answer=="No":
            break
        if answer=="yes" or answer=="Yes":
            rWord=pickAword()
            print rWord
            guessALetter(rWord)

        answer=raw_input('Do you want to play the Hangman game again? enter yes or no :')

