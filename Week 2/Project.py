# "Guess the number" mini-project
# Needed modules
import simplegui
import math
import random

# Needed global variables
max = 100
min = 0
count = 0
n = 0
answer = 0

# Helper Function
def new_game():
    """ Function used when initializing a new game """
    global n, answer
    n = math.ceil(math.log(max - min + 1, 2))
    answer = random.randrange(min, max)
    print 'New game! Range is from ' + str(min) + ' to ' + str(max) + '.'
    print 'Number of remaining guesses is: ' + str(int(n))
    print ''

# Event Handlers
def range100():
    """ Button that changes the range to [0,100) and starts a new game """ 
    global max
    max = 100
    new_game()

def range1000():
    """ Button that changes the range to [0,1000) and starts a new game """     
    global max
    max = 1000
    new_game()
    
def input_guess(guess):
    """ Handler for the input guess """	
    global n
    num_guess = float(guess)
    
    # Is the number in the current range?
    if num_guess < min or num_guess >= max:
        print 'Your guess is not inside the range of this game!'
    # It is:
    else:
        print 'Guess was ' + guess + '.'
        if num_guess < answer:
            print 'Higher!'
        elif num_guess > answer:
            print 'Lower!'
        else:
            print 'Correct!'
            print
            new_game()
            return
        
    # Computing remaining number of guesses, when failing to guess    
    n = n - 1
    if n == 0:
        print 'Game Over! The answer was ' + str(answer) + '.'
        print ''
        new_game()
        return
    print 'Number of remaining guesses is ' + str(int(n)) + '.'
    print ''
    
# Create frame
frame = simplegui.create_frame('Guess the number!', 0, 150, 200)

# Register event handlers for control elements and start frame
frame.add_button('Range is [0, 100)', range100, 150)
frame.add_button('Range is [0, 1000)', range1000, 150)
frame.add_input('Enter a guess', input_guess, 150)
frame.start()

# Call new_game 
new_game()
