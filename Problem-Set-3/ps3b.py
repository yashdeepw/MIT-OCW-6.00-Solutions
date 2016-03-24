from ps3a import *
import time
from perm import *


#
#
# Problem #6A: Computer chooses a word
#
#
def comp_choose_word(hand, word_list):
    """
	Given a hand and a word_dict, find the word that gives the maximum value score, and return it.
   	This word should be calculated by considering all possible permutations of lengths 1 to HAND_SIZE.

    hand: dictionary (string -> int)
    word_list: list (string)
    """
    possible_words = []
    maxScore = 0
    maxWord = None
    for i in range ( HAND_SIZE , 1, -1):
        perms = get_perms (hand,i)
        possible_words.extend(perms)
    for word in possible_words:
        if word in word_list:
            word_score = get_word_score(word, HAND_SIZE)
            if ( word_score > maxScore) :
                maxScore = word_score
                maxWord = word
    return maxWord
                
        

#
# Problem #6B: Computer plays a hand
#
def comp_play_hand(hand, word_list):
    """
     Allows the computer to play the given hand, as follows:

     * The hand is displayed.

     * The computer chooses a word using comp_choose_words(hand, word_dict).

     * After every valid word: the score for that word is displayed, 
       the remaining letters in the hand are displayed, and the computer 
       chooses another word.

     * The sum of the word scores is displayed when the hand finishes.

     * The hand finishes when the computer has exhausted its possible choices (i.e. comp_play_hand returns None).

     hand: dictionary (string -> int)
     word_list: list (string)
    """
    total_score = 0
    n  =  calculate_handlen(hand)
    
    while ( calculate_handlen(hand) != 0 ):
        print 'Current hand:',
        display_hand(hand)
        word = comp_choose_word(hand, word_list)
        if ( word == None):
            print "Computer couldn't make any more words."
            break
        word_score = get_word_score(word, n )
        total_score += get_word_score(word, n )
        hand = update_hand(hand, word)
        print 'Computer chose: ' + word
        print word, 'earned', word_score, 'points. Total:', total_score, 'points.'
        print
        
    print "Computer's total score:", total_score, 'points.'
    
#
# Problem #6C: Playing a game
#
#
def play_game(word_list):
    """Allow the user to play an arbitrary number of hands.

    1) Asks the user to input 'n' or 'r' or 'e'.
    * If the user inputs 'n', play a new (random) hand.
    * If the user inputs 'r', play the last hand again.
    * If the user inputs 'e', exit the game.
    * If the user inputs anything else, ask them again.

    2) Ask the user to input a 'u' or a 'c'.
    * If the user inputs 'u', let the user play the game as before using play_hand.
    * If the user inputs 'c', let the computer play the game using comp_play_hand (created above).
    * If the user inputs anything else, ask them again.

    3) After the computer or user has played the hand, repeat from step 1

    word_list: list (string)
    """
    hand = deal_hand(HAND_SIZE)

    while True:

        cmd = raw_input('Enter n to deal a new hand, r to replay the last hand, or e to end game: ')
        while cmd != 'n' and cmd != 'r' and cmd != 'e':
            print "Invalid command."
            cmd = raw_input('Enter n to deal a new hand, r to replay the last hand, or e to end game: ')
        
        if cmd == 'e':
            break 
 
        player = raw_input('Enter u to have yourself play, c to have the computer play: ')
        while player != 'u' and player != 'c':
            print "Invalid command."
            player = raw_input('Enter u to have yourself play, c to have the computer play: ')

        if cmd == 'n':
            hand = deal_hand(HAND_SIZE)
	    
        if player == 'u':
            play_hand(hand.copy(), word_list)
        else:
            comp_play_hand(hand.copy(), word_list)
        
#
# Build data structures used for entire session and play game
#
if __name__ == '__main__':
    word_list = load_words()
    play_game(word_list)
