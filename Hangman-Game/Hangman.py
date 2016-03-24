# 6.00 Problem Set 3
# 
# Hangman
#


# -----------------------------------
# Helper code
# (you don't need to understand this helper code)
import random
import string

WORDLIST_FILENAME = "words.txt"

def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = string.split(line)
    print "  ", len(wordlist), "words loaded."
    return wordlist

def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# actually load the dictionary of words and point to it with 
# the wordlist variable so that it can be accessed from anywhere
# in the program
wordlist = load_words()

# your code begins here!
word =  choose_word(wordlist)
print 'Welcome to the game, Hangman!'
print ''
print 'I am thinking of a word that is ' +  str(len(word)) + ' letters long.'
print ''

guess_left = 8
guess_tup = ('_ ',)*len(word)
guess = ''
guessed = ''
p = ()
new = ()


def avail_letter( p ):
    abc = ('a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z')
    print 'Available Letters : '
    for i in abc:
        if ( not tuple_search(i,p)):
            print i,
    print ''

def collect( tup ):
    guess = ''
    for i in tup:
        global guess
        guess += i
    return guess

def mut_tup ( tup, char):
    global new
    for i in range (max(len(word), len(tup))):
        if ( i < len(word) and word[i] == char):
            new += (char + ' ' ,)
        else:
            new =  new + (tup[i],)
    return new[-len(word):]
    
def tuple_search( a , tupl):
    for i in tupl:
        if ( i == a ):
            return True
    return False 

def guess_letter( p ):
    x = raw_input('Please guess a letter: ')
    while ( (not (x.isalpha() and len(x) == 1 )) or tuple_search( x, p ) ):
        print 'Give a valid guess i.e. a single alphabet which you did not guess already.'
        x = raw_input('Please guess a letter: ')
    x = x.lower()
    return x

def guess_check( a, guess_left):
    global guess
    if ( guess_left == 0):
        print "You used all your chances and didn't guess the word."
        print 'You Lost!.'
        print 'The word was : ' + word.upper()
    elif ( a[-1] in word ):
        global guess_tup
        guess_tup = mut_tup(guess_tup,a[-1])
        guess = collect (guess_tup)
        print 'Good guess : '+ guess
        print '------------------------------------------------------'
        return guess_left
        
    else:
        print 'Oops! That letter is not in my word: '+ guess
        print '------------------------------------------------------'
        guess_left -= 1
        return guess_left

def collect_guess( guess ):
    global guessed
    guessed = ''
    for i in guess:
        if ( i != ' ' ):
            guessed += i
    return guessed

while ( guessed != word ):
    if   (guess_left == 0):
        print "You used all your chances and didn't guess the word."
        print 'You Lost!.'
        print 'The word was : ' + word.upper()
        break
    elif (guess_left == 1):
        print 'You have only 1 guess left.'
        p = p + (guess_letter(p),)
        avail_letter( p )
        guess_left = guess_check( p , guess_left)
    else:
        print 'You have ' + str(guess_left) +' guesses left.'
        p = p + (guess_letter(p),)
        avail_letter( p )
        guess_left = guess_check( p , guess_left)
        collect_guess ( guess )
        
if (guessed == word):
    print 'You Won!.'
