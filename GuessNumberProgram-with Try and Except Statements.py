#This is a guess the number game.
import random

print('Hello. What is your name?')
name = input()

print('Well, ' + name + ', I am thinking of a number between 1 & 20')
secretNumber = random.randint(1, 20)
#secretNumber = Variable that will choose an integer randomly between 1 & 20.

#range(1, 7) will be a random range between 1 & 7
#guess = int(input()) will convert any input into an integer
#break will break the else if loop and end the for in loop
for guessesTaken in range(1, 7):
    print('Take a guess.')
    guess = int(input())
    def guessesTaken(guess):
        try: #need to figure out this except statement to make a specific error exception occur
            return guess == guessesTaken
        except ValueError:
            print('Error: Please put an integer!')

    if guess < secretNumber:
        print('Your guess is too low.')
    elif guess > secretNumber:
        print('Your guess is too high.')
    else:
        break

#str(guessesTaken) & str(secretNumber) are put as strings as they are originally put as integers
if guess == secretNumber:
    print('Good job, ' + name + '! You guessed my number in ' + str(guessesTaken) + ' guesses!')
else:
    print('Nope. The number I was thinking of was ' + str(secretNumber))
    
print('You took ' +str(guessesTaken) + ' guesses.')
