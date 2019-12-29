import random

def game():

    
    print('What is your name?')
    name = input()
    print('Welcome to the game ' + name +'. Your mission is to guess the number between 1 and 10. You have 3 chances.')

    guessesMade = 0
    number = random.randint(1, 10)

    for guessesMade in range(3):
        print('What is your guess?')
        guess = input()
        guess = int(guess)
        
        if guess < number:
            print('The number you are looking for is higher than that!')
        
        if guess > number:
            print('The number you are looking for is lower than that!')
        
        if guess == number:
            print('You picked the right number! Good work!')
            break

    if guess == number:
        guessesMade =str(guessesMade +1)
        print('Good work ' + name + '. You got it right in ' + guessesMade +' guesses!')

    if guess != number:
        number = str(number)
        print('Sorry, you lost. The number was ' + number + '.')
    

    print('Would you like to play again? (y/n): ')
    answer = input()
    
    if answer == "y":
        game()
    
    print('Goodbye')
       
